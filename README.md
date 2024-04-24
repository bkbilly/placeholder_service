# Placeholder Service
This is a Python script that creates images from text input received through HTTP requests.

## Features
 - Generates images with user-provided text.
 - Supports various image formats (PNG by default).
 - Allows customization of font, text color, background color, font size, and alignment.
 - Fetches fonts from Google Fonts repository if not found locally.

## Usage

### Server:
 - Save the script as `placeholder_service.py`.
 - Install required libraries:
```bash
pip install -r requirements.txt
```

Run the server:
```bash
python placeholder_service.py
```
This will start the server on http://localhost:9845 by default.

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

## Configuration

### Font Download:
By default, the server tries to download fonts from the Google Fonts repository if the requested font is not found locally.
This functionality requires an internet connection.

### Logging:
The script uses Python's built-in logging module. You can configure logging behavior by creating a separate logging configuration file.

## Development
Feel free to modify the script to suit your specific needs. You can add functionalities like:
 - Additional image processing options.
 - User authentication for secure text submission.
 - Support for different text formats (e.g., HTML).

## License
This project is licensed under the MIT License. See the LICENSE file for details.
