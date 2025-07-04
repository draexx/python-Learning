import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add the parent directory of pySample to the Python path
# to allow importing pyTesseractSample
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Now we can import the module from pySample
from pySample import pyTesseractSample

class TestPytesseractSample(unittest.TestCase):

    def test_ocr_image_file_not_found(self):
        """
        Test that ocr_image returns an error message if the image file does not exist.
        """
        non_existent_file = "non_existent_image.png"
        expected_message = f"Image not found: {non_existent_file}"
        self.assertEqual(pyTesseractSample.ocr_image(non_existent_file), expected_message)

    @patch('pySample.pyTesseractSample.cv2.imread')
    def test_ocr_image_read_error(self, mock_imread):
        """
        Test that ocr_image returns an error message if cv2.imread fails to read the image.
        """
        mock_imread.return_value = None
        test_file = "dummy_image.png" # File needs to exist for os.path.exists check

        # Create a dummy file for the os.path.exists check to pass
        with open(test_file, 'w') as f:
            f.write("dummy content")

        expected_message = f"Could not read image (possibly corrupted or unsupported format): {test_file}"
        self.assertEqual(pyTesseractSample.ocr_image(test_file), expected_message)

        os.remove(test_file) # Clean up dummy file

    @patch('pySample.pyTesseractSample.pytesseract.image_to_string')
    @patch('pySample.pyTesseractSample.cv2.imread')
    def test_ocr_image_success(self, mock_imread, mock_image_to_string):
        """
        Test successful OCR processing.
        """
        # Mock cv2.imread to return a dummy image object (MagicMock can simulate this)
        mock_imread.return_value = MagicMock()

        # Mock pytesseract.image_to_string to return expected text
        expected_text = "Hello World"
        mock_image_to_string.return_value = expected_text

        test_file = "another_dummy_image.png"
        with open(test_file, 'w') as f:
            f.write("dummy content for success test")

        # Call the function
        result = pyTesseractSample.ocr_image(test_file)

        # Assertions
        self.assertEqual(result, expected_text)
        mock_imread.assert_called_once_with(test_file)
        mock_image_to_string.assert_called_once_with(mock_imread.return_value)

        os.remove(test_file) # Clean up

    @patch('pySample.pyTesseractSample.pytesseract.image_to_string')
    @patch('pySample.pyTesseractSample.cv2.imread')
    def test_ocr_image_no_text_detected(self, mock_imread, mock_image_to_string):
        """
        Test OCR processing when no text is detected in the image.
        """
        mock_imread.return_value = MagicMock()
        mock_image_to_string.return_value = "" # Simulate no text detected

        test_file = "empty_text_image.png"
        with open(test_file, 'w') as f:
            f.write("dummy content for no text test")

        result = pyTesseractSample.ocr_image(test_file)

        self.assertEqual(result, "No text detected")
        os.remove(test_file)

    @patch('pySample.pyTesseractSample.pytesseract.image_to_string')
    @patch('pySample.pyTesseractSample.cv2.imread')
    def test_ocr_image_pytesseract_exception(self, mock_imread, mock_image_to_string):
        """
        Test how ocr_image handles an exception from pytesseract.
        """
        mock_imread.return_value = MagicMock()
        error_message = "Tesseract error"
        mock_image_to_string.side_effect = Exception(error_message)

        test_file = "exception_image.png"
        with open(test_file, 'w') as f:
            f.write("dummy content for exception test")

        expected_response = f"Error during OCR for {test_file}: {error_message}"
        result = pyTesseractSample.ocr_image(test_file)

        self.assertEqual(result, expected_response)
        os.remove(test_file)

if __name__ == '__main__':
    unittest.main()
