import unittest
from PIL import Image
import image_checks

class ImageChecksTests(unittest.TestCase):
    def test_is_good_aspect_ratio(self):
        # Test case 1: Image with aspect ratio within the range
        img1 = Image.new('RGB', (1920, 1080))
        self.assertTrue(ImageChecks.is_good_aspect_ratio(img1))

        # Test case 2: Image with aspect ratio below the range
        img2 = Image.new('RGB', (800, 600))
        self.assertFalse(ImageChecks.is_good_aspect_ratio(img2))

        # Test case 3: Image with aspect ratio above the range
        img3 = Image.new('RGB', (1080, 1920))
        self.assertFalse(ImageChecks.is_good_aspect_ratio(img3))

        # Test case 4: Image with square aspect ratio
        img4 = Image.new('RGB', (1000, 1000))
        self.assertFalse(ImageChecks.is_good_aspect_ratio(img4))

if __name__ == '__main__':
    unittest.main()