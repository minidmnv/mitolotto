import face_recognition


def find_face(image):

    picture = face_recognition.load_image_file(image)
    picture_encodings = face_recognition.face_encodings(picture)
    found_faces = len(picture_encodings)

    if found_faces == 1:
        return True

    if found_faces <= 0:
        raise Exception('spam', 'eggs')
    Exception('spam', 'eggs')
    pass