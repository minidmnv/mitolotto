import unittest
import utils

from os import remove
from PIL import Image
from exceptions import NoFaceFoundError
from exceptions import TooManyFacesFoundError


class TestFindFunction(unittest.TestCase):

    def test_find_face(self):
        result = utils.find_face("./images/obama.jpg")
        self.assertTrue(result)

    def test_not_finding_face(self):
        self.assertRaises(NoFaceFoundError, utils.find_face, "./images/no_face.jpg")

    def test_too_many_faces(self):
        self.assertRaises(TooManyFacesFoundError, utils.find_face, "./images/group.jpg")


class TestCompareFunction(unittest.TestCase):

    def test_compare_not_same_faces(self):
        result = utils.compare_faces("./images/obama.jpg", "./images/biden.jpg")
        self.assertFalse(result)

    def test_compare_same_face(self):
        result = utils.compare_faces("./images/obama.jpg", "./images/obama2.jpg")
        self.assertTrue(result)


class TestResizeFunction(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        try:
            remove("./tmp/obama_r.jpg")
        except OSError as error:
            print(error)

    def test_resize(self):
        utils.resize_image("./images/obama.jpg", "./tmp/obama_r.jpg")
        img = Image.open("./tmp/obama_r.jpg")
        self.assertEqual(500, img.height)
        self.assertEqual(400, img.width)


if __name__ == '__main__':
    unittest.main()
