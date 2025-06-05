import os
import argparse
import cv2

# Set up argument parser
parser = argparse.ArgumentParser(description="Resize images in a folder with high-quality settings.")
parser.add_argument("input_folder", help="Path to the input folder containing images.")
parser.add_argument("output_folder", help="Path to the output folder where resized images will be saved.")
parser.add_argument("resolution", type=int, nargs=2, metavar=('width', 'height'),
					help="Target resolution for resizing (width height).")
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
	if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
		continue

	src_path = os.path.join(input_folder, filename)
	dst_path = os.path.join(output_folder, filename)

	# Load image with cv2
	img = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
	if img is None:
		print(f"Skipping {filename}: unable to read.")
		continue

	# Get image size
	height, width = img.shape[:2]
	if (width, height) == resolution:
		print(f"Skipping {filename}: already at resolution {resolution}")
		continue

	# Resize with high-quality interpolation
	resized = cv2.resize(img, resolution, interpolation=cv2.INTER_LANCZOS4)

	# Determine file extension
	ext = os.path.splitext(filename)[1].lower()

	# Save with format-specific parameters
	if ext in (".jpg", ".jpeg"):
		cv2.imwrite(dst_path, resized, [cv2.IMWRITE_JPEG_QUALITY, 80])
	elif ext == ".png":
		cv2.imwrite(dst_path, resized, [cv2.IMWRITE_PNG_COMPRESSION, 3])
	elif ext == ".webp":
		cv2.imwrite(dst_path, resized, [cv2.IMWRITE_WEBP_QUALITY, 95])
	else:
		cv2.imwrite(dst_path, resized)

	print(f"Resized {filename} to {resolution}")

print("Batch resizing completed!")
