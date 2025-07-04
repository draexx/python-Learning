import cv2
import os
import pytesseract
# Unused imports: sys, webbrowser, platform. Removed for cleanliness.

def ocr_image(image_path):
    """
    Performs OCR on an image and returns the extracted text.
    If the image is not found or OCR fails, it returns an error message.
    """
    if not os.path.exists(image_path):
        return f"Image not found: {image_path}"
    try:
        img = cv2.imread(image_path)
        if img is None: # Check if image loading failed
            return f"Could not read image (possibly corrupted or unsupported format): {image_path}"
        text = pytesseract.image_to_string(img)
        return text.strip() if text else "No text detected"
    except Exception as e:
        return f"Error during OCR for {image_path}: {e}"

def main():
    """
    Main function to demonstrate OCR on sample images.
    """
    # It's good practice to define paths relative to the script location
    # or use absolute paths if necessary and configurable.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    img_folder = os.path.join(script_dir, "img")

    image_files = ["example_02.png", "example_02.jpg"]

    print(f"Image folder path: {img_folder}\n")

    for img_file in image_files:
        image_path = os.path.join(img_folder, img_file)
        print(f"Processing: {image_path}")
        extracted_text = ocr_image(image_path)
        print(f"Extracted text:\n---\n{extracted_text}\n---\n")

if __name__ == "__main__":
    # Note: For pytesseract to work, Tesseract OCR must be installed on the system
    # and pytesseract needs to know where to find it (often by adding tesseract to PATH).
    # Example for Windows (if not in PATH):
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    main()