# Placeholder Service
This is a Python script that creates images from text input received through HTTP requests.

## Features
 - Generates images with user-provided text.
 - Supports various image formats (PNG by default).
 - Allows customization of font, text color, background color, font size, and alignment.
 - Fetches fonts from Google Fonts repository if not found locally.

## Usage

### Client:

You can use any tool that can send HTTP requests, such as curl or a web browser. Here's an example using curl:

```bash
curl "http://localhost:9845/?text=YOUR_TEXT&font=FONT_NAME.ttf&color_text=COLOR_CODE&color_bg=COLOR_CODE&font_size=SIZE&font_align=ALIGN&img_format=FORMAT"

# Replace with your desired options:
#  - text: The text to be displayed on the image (required)
#  - font: Path to a font file (optional, defaults to 'FrederickatheGreat-Regular.ttf')
#  - color_text: Text color in hex code (e.g., 'FF0000' for red, optional, defaults to '1400FF')
#  - color_bg: Background color name or hex code (optional, defaults to 'white')
#  - font_size: Font size in pixels (optional, defaults to 200)
#  - font_align: Horizontal text alignment ('left', 'center', or 'right', optional, defaults to 'center')
#  - img_format: Image format (e.g., 'png', 'jpg', etc., optional, defaults to 'png')
```

### Example:

```bash
curl "http://localhost:9845/?text=Hello\nWorld!&color_text=00FF00&color_bg=0000FF"
```

This will download an image with the text "Hello\nWorld!" in green color and in blue background.
