import face_recognition
import numpy as np

def photoID_format(img):
    # Get the face location 
    face = face_recognition.face_locations(np.array(img)) 
    # face = [(top, right, bottom, left)] --> CSS rule (top, right, bottom, left)
    # Convert from list of tuple to list
    coord = [item for t in face for item in t]

    box_size = coord[2] - coord[0]
    box_size /= 2
    width, height = img.size[0], img.size[1]

    # Initial Assign
    left = coord[3] - box_size
    top = coord[0] - box_size 
    right = coord[1] + box_size 
    bottom = coord[2] + (3*box_size)

    # Image out of bounds check
    left = left if left >= 0 else 0
    top = top if top >= 0 else 0
    right = right if right <= width else width
    bottom = bottom if bottom <= height else height

    # Crop the image with roughly 3:4 aspect ratio
    img = img.crop((left, top, right, bottom))
    img = img.resize((150,200))

    return img

if __name__ == "__main__":
    pass