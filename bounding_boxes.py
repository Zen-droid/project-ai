import face_recognition
import cv2
import attendance_window

def draw_bounding_box(img, face_bounding_box):
    top, right, bottom, left = face_bounding_box[0], face_bounding_box[1], face_bounding_box[2], face_bounding_box[3]
    w = right-left
    h = bottom-top

    # top-left
    img = cv2.line(img, (left, top), (left+int(w*0.3), top), (127,127,127), 2)
    img = cv2.line(img, (left, top), (left, top+int(h*0.3)), (127,127,127), 2)
    #top-right
    img = cv2.line(img, (right, top), (right-int(w*0.3), top), (127,127,127), 2)
    img = cv2.line(img, (right, top), (right, top+int(h*0.3)), (127,127,127), 2)
    #bottom-left
    img = cv2.line(img, (left, bottom), (left+int(w*0.3), bottom), (127,127,127), 2)
    img = cv2.line(img, (left, bottom), (left, bottom-int(h*0.3)), (127,127,127), 2)
    #bottom-right
    img = cv2.line(img, (right, bottom), (right-int(w*0.3), bottom), (127,127,127), 2)
    img = cv2.line(img, (right, bottom), (right, bottom-int(h*0.3)), (127,127,127), 2)

    return img


def draw_overlay(img):
    curr_time = attendance_window.get_curr_time()
    face_bounding_box = face_recognition.face_locations(img)

    if face_bounding_box:
        img = draw_bounding_box(img, face_bounding_box[0])

    img = cv2.putText(img, curr_time, (0,20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,0))

    return img

if __name__ == "__main__":
    pass