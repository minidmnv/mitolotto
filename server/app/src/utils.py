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


def compare_faces(known_image_path, unknown_image_path):
    known_image = face_recognition.load_image_file(known_image_path)
    unknown_image = face_recognition.load_image_file(unknown_image_path)

    known_image_encoding =  face_recognition.face_encodings(known_image)[0]
    unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

    return face_recognition.compare_faces(known_image_encoding, unknown_image_encoding)

