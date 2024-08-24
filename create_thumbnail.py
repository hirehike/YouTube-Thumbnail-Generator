from PIL import Image, ImageDraw, ImageFont
import textwrap

# Load the background image from the assets folder
# background = Image.open("assets/background.jpg")

# Create a light blue gradient background
width, height = 1280, 720
background = Image.new("RGB", (width, height), "#2A5D84")

# Ensure the background image is the correct size (1280x720)
background = background.resize((1280, 720))

# Create a drawing object
draw = ImageDraw.Draw(background)

# Load a font with 90px size
try:
    font = ImageFont.truetype("fonts/BungeeTint-Regular.ttf", 90)
except IOError:
    font = ImageFont.load_default()

# Define the text you want to add
text = "How to create YouTube thumbnails using Python?"

# Wrap the text to fit within the image width
max_width = 1200  # Max width for text in pixels
wrapped_text = textwrap.fill(text, width=20)

# Calculate the text size
text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Calculate the position to center the text
text_position = ((1280 - text_width) // 2, (720 - text_height) // 2)

# Add the wrapped text in white at the center
draw.text(text_position, wrapped_text, font=font, fill=(255, 255, 255))

# Load the company logo
logo = Image.open("assets/logo.jpg").convert("RGBA")

# Resize the logo if necessary (e.g., 150x150 pixels)
logo = logo.resize((100, 100))

# Calculate the position for the logo at the bottom right corner
logo_position = (1280 - logo.width - 20, 720 - logo.height - 20)

# Paste the logo onto the background
background.paste(logo, logo_position, logo)

# Load the Python logo
python_logo = Image.open("assets/python.jpg").convert("RGBA")

# Resize the Python logo if necessary (e.g., 100x100 pixels)
python_logo = python_logo.resize((250, 250))

# Calculate the position for the Python logo at the top right corner
python_logo_position = (1280 - python_logo.width - 50, 50)

# Paste the Python logo onto the background
background.paste(python_logo, python_logo_position, python_logo)

# Save the thumbnail
background.save("thumbnails/thumbnail_with_logo.png")

print("Thumbnail with wrapped text and logo created successfully!")
