import unittest
from PIL import Image
from brightness import calculate_brightness, get_images_brightness


class TestBrightnessMethods(unittest.TestCase):
    def setUp(self):
        self.images = []
        self.images.append(Image.open("./resources/images/white.png"))
        self.images.append(Image.open("./resources/images/black.png"))
        self.images.append(Image.open("./resources/images/scrum_logo.jpg"))

    def test_calculate_brightness(self):
        self.assertEqual(calculate_brightness(self.images[0]), 1, "The value obtained are not correct !!!")
        self.assertEqual(calculate_brightness(self.images[1]), 0, "The value obtained are not correct !!!")
        self.assertLessEqual(calculate_brightness(self.images[2]) - 0.91, 0.001,
                             "The value obtained are not correct !!!")

    def test_get_images_brightness(self):
        images_brightness = get_images_brightness(self.images)
        self.assertEqual(images_brightness[0], 1, "The value obtained are not correct !!!")
        self.assertEqual(images_brightness[1], 0, "The value obtained are not correct !!!")
        self.assertLessEqual(images_brightness[2] - 0.91, 0.001, "The value obtained are not correct !!!")


if __name__ == '__main__':
    unittest.main()