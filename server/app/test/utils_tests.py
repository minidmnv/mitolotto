import unittest
import utils
from PIL import Image
from exceptions import NoFaceFoundError
from exceptions import TooManyFacesFoundError


class TestFindFunction(unittest.TestCase):

    def test_find_face(self):
        result = utils.find_face("./obama.jpg")
        self.assertTrue(result)

    def test_not_finding_face(self):
        self.assertRaises(NoFaceFoundError, utils.find_face, "./no_face.jpg")

    def test_too_many_faces(self):
        self.assertRaises(TooManyFacesFoundError, utils.find_face, "./group.jpg")


class TestCompareFunction(unittest.TestCase):

    def test_compare_not_same_faces(self):
        result = utils.compare_faces("./obama.jpg", "./biden.jpg")
        self.assertFalse(result)

    def test_compare_same_face(self):
        result = utils.compare_faces("./obama.jpg", "./obama2.jpg")
        self.assertTrue(result)


class TestResizeFunction(unittest.TestCase):

    def test_resize(self):
        utils.resize_image("./obama.jpg", "./obama_r.jpg")
        img = Image.open("./obama_r.jpg")
        self.assertEqual(500, img.height)
        self.assertEqual(400, img.width)


if __name__ == '__main__':
    unittest.main()
