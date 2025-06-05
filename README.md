### Pre-requisites

Make sure you have the OpenCV library installed:

```bash
pip install opencv-python
```

---

### Running the Script

1. **Open a Terminal or Command Prompt:**
   Navigate to the directory where the script (`image_batch_resize.py`) is located.

2. **Execute the Script with the Required Arguments:**
   The script requires three arguments:

   * **input\_folder:** The folder path containing the images to resize.
   * **output\_folder:** The folder path where resized images will be saved.
   * **resolution:** The target resolution (width and height) for the images.

   **Example command:**

   ```bash
   python image_batch_resize.py "C:\path\to\input_folder" "C:\path\to\output_folder" 256 256
   ```