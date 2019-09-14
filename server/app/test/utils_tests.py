import unittest
import utils
from exceptions import NoFaceFoundError
from exceptions import TooManyFacesFoundError


class TestCompareFunction(unittest.TestCase):

    def test_find_face(self):
        result = utils.find_face("./obama.jpg")
        self.assertTrue(result)

    def test_not_finding_face(self):
        self.assertRaises(NoFaceFoundError, utils.find_face, "./no_face.jpg")

    def test_too_many_faces(self):
        self.assertRaises(TooManyFacesFoundError, utils.find_face, "./group.jpg")


if __name__ == '__main__':
    unittest.main()
