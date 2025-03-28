import os
import argparse
from PIL import Image

# Set up argument parser
parser = argparse.ArgumentParser(description="Resize images in a folder.")
parser.add_argument("input_folder", help="Path to the input folder containing images.")
parser.add_argument("output_folder", help="Path to the output folder where resized images will be saved.")
parser.add_argument("resolution", type=int, nargs=2, metavar=('width', 'height'), help="Target resolution for resizing (width height).")
args = parser.parse_args()

# Get the input folder, output folder, and resolution from command-line arguments
input_folder = args.input_folder
output_folder = args.output_folder
resolution = tuple(args.resolution)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".png", ".jpg", ".jpeg", ".webp")):  # Add other formats if needed
        img_path = os.path.join(input_folder, filename)
        
        # Open the image
        img = Image.open(img_path)
        
        # Resize the image to the specified resolution
        img_resized = img.resize(resolution, Image.LANCZOS)
        
        # Save the resized image
        img_resized.save(os.path.join(output_folder, filename))
        
        print(f"Resized {filename} to {resolution}")

print("Batch resizing completed!")
