"""Asterisk Call Status helper."""
import json
import os
import logging
from io import BytesIO
from pathlib import Path

from urllib import request
from PIL import Image, ImageFont, ImageDraw, ImageColor
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


_LOGGER = logging.getLogger(__name__)


def load_font(request_font: str):
    """Loads a font from local directory or downloads from Google Fonts.

    Args:
      request_font: The requested font filename.

    Returns:
      The path to the loaded font file. Returns None if font cannot be found
      or downloaded.
    """

    font_directory = Path(__file__).parent
    font_path = f"{font_directory}/{request_font}"
    github_url = "https://raw.githubusercontent.com/google/fonts/main/"
    github_tree_url = "https://api.github.com/repos/google/fonts/git/trees/main?recursive=1"
    if os.path.isfile(font_path):
        return font_path
    else:
        with request.urlopen(github_tree_url) as url:
            tree_items = json.load(url)
            for tree_item in tree_items["tree"]:
                if request_font in tree_item["path"]:
                    try:
                        _LOGGER.debug(f"Downloading font: {tree_item['path']}")
                        request.urlretrieve(f"{github_url}{tree_item['path']}", font_path)
                        return font_path
                    except Exception as ex:
                        _LOGGER.error(f"Can't download font", exc_info=ex)
                        return None
    _LOGGER.error(f"Can't find font")
    return None


def text_to_image(
        text: str,
        font: str = "FrederickatheGreat-Regular",
        width: int = 1024,
        height: int = 600,
        color_text: str = "1400FF",
        color_bg: str = "white",
        font_size: int = 200,
        font_align: str = "center",
        img_format: str = "png",
        **kwargs) -> bytes:
    """Converts text to an image with various customization options.

    Args:
        text: The text to be displayed on the image. (required)
        font: Path to the desired font file. (default: "FrederickatheGreat-Regular")
        width: Width of the image in pixels. (default: 1024)
        height: Height of the image in pixels. (default: 600)
        color_text: Text color name or hex code. (default: "1400FF")
        color_bg: Background color name or hex code. (default: "white")
        font_size: Maximum font size. (default: 200)
        font_align: Horizontal text alignment within the image. (default: "center")
            Options: "left", "center", "right"
        img_format: Format of the generated image. (default: "PNG")
            Supported formats depend on PIL library capabilities.

    Returns:
        The generated image as a byte stream. Returns None if there's an error.
    """
    # Fix input types
    width = int(width)
    height = int(height)
    font_size = int(font_size)
    text = text.replace("\\n", "\n")
    if color_text not in ImageColor.colormap:
        color_text = "#" + color_text
    if color_bg not in ImageColor.colormap:
        color_bg = "#" + color_bg
    if font[-4:] != ".ttf":
        font += ".ttf"

    # Create image
    img = Image.new("RGB", (width, height), color=color_bg)
    draw = ImageDraw.Draw(img)
    font_path = load_font(font)
    if font_path is None:
        return None
    while True:
        truefont = ImageFont.truetype(font_path, size=font_size)
        _, _, font_width, font_height = draw.textbbox((0, 0), text, font=truefont)
        if font_width < width and font_height < height:
            break
        font_size -= 15
    draw_point = (
        int((width - font_width) / 2),
        int((height - font_height) / 2)
    )
    draw.text(draw_point, text, font=truefont, fill=color_text, align=font_align)
    with BytesIO() as f:
        img.save(f, format=img_format)
        return f.getvalue()


class TextImageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters as a dictionary
        query_dict = dict(parse_qsl(urlparse(self.path).query))

        if urlparse(self.path).path in ["/", ""]:
            if "text" in query_dict:
                # Create a new image
                img_data = text_to_image(**query_dict)
                if img_data is not None:
                    # Set response headers
                    img_format = query_dict.get("img_format", "png")
                    self.send_response(200)
                    self.send_header("Content-Type", f"image/{img_format}")
                    self.send_header("Content-Length", str(len(img_data)))
                    self.end_headers()

                    # Send image data
                    self.wfile.write(img_data)
            else:
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(text_to_image.__doc__.encode("UTF-8"))


if __name__ == "__main__":
    HOST_NAME = "0.0.0.0"
    PORT_NUMBER = 9845
    server_address = (HOST_NAME, PORT_NUMBER)
    httpd = HTTPServer(server_address, TextImageHandler)
    print("Server started http://%s:%s" % (HOST_NAME, PORT_NUMBER))
    httpd.serve_forever()
