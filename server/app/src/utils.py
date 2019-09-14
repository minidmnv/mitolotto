import face_recognition
from PIL import Image
from exceptions import NoFaceFoundError
from exceptions import TooManyFacesFoundError


def resize_image(source_path, destination_path):
    image = Image.open(source_path)
    image.thumbnail((500, 500))
    image.save(destination_path)


def find_face(image):
    picture = face_recognition.load_image_file(image)
    picture_encodings = face_recognition.face_encodings(picture)
    found_faces = len(picture_encodings)

    if found_faces == 1:
        return True

    if found_faces <= 0:
        raise NoFaceFoundError
    raise TooManyFacesFoundError
    pass


def compare_faces(known_image, unkown_image):
    pass

