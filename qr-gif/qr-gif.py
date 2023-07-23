import os
from PIL import Image

# Directory containing the PNG files
png_directory = "js_grid"

# List all PNG files in the directory
png_files = [f for f in os.listdir(png_directory) if f.endswith(".png")]

# Sort the list of files (optional but ensures the frames are in order)
png_files.sort()

# Create an empty list to store image objects
images = []

# Open each PNG file, add it to the images list
for png_file in png_files:
    image_path = os.path.join(png_directory, png_file)
    img = Image.open(image_path)
    images.append(img)

# Convert the images to RGB mode
for i, img in enumerate(images):
    images[i] = img.convert("RGB")

# Save the images as an animated GIF
output_gif_path = "output.gif"
duration = 5000  # Duration for each frame in milliseconds (5 seconds)

# Save the images as an animated GIF with the given duration between frames
images[0].save(
    output_gif_path,
    save_all=True,
    append_images=images[1:],
    duration=duration,
    loop=0,  # Loop forever (0 means no loop, any other value is the number of loops)
)
