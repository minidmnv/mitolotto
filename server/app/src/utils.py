import base64
import io

import face_recognition

from PIL import Image
from exceptions import NoFaceFoundError
from exceptions import TooManyFacesFoundError
from exceptions import EmptyOrMissingPictureError


def resize_image(source):
    image = Image.open(source)
    image.thumbnail((500, 500))

    with io.BytesIO() as output:
        image.save(output, image.format)
        return io.BytesIO(output.getvalue())


def find_face(image):
    picture = face_recognition.load_image_file(image)
    picture_encodings = face_recognition.face_encodings(picture)
    found_faces = len(picture_encodings)

    if found_faces == 1:
        return True

    if found_faces <= 0:
        raise NoFaceFoundError('There is no person on your photo')
    raise TooManyFacesFoundError('There are too many people on your photo')


def compare_faces(raw_known_image, raw_unknown_image):
    known_image = face_recognition.load_image_file(raw_known_image)
    unknown_image = face_recognition.load_image_file(raw_unknown_image)

    known_image_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

    return face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)[0]


def decode_img(image_base64):
    if not image_base64 or len(image_base64) <= 0:
        raise EmptyOrMissingPictureError('Your photo is missing or empty')

    if type(image_base64) is str and "data:image/png;base64," in image_base64:
        image_base64 = image_base64.replace("data:image/png;base64,", "")
    image_base64 = base64.b64decode(image_base64)
    return resize_image(io.BytesIO(image_base64))


def encode_img(image):
    with open(image, "rb") as image_file:
        return base64.b64encode(image_file.read())
