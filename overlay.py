import face_recognition
import cv2
import attendance_window
import FaceRecognition

def draw_bounding_box(img):
    face_bounding_box = face_recognition.face_locations(img)

    if face_bounding_box:
        top, right, bottom, left = face_bounding_box[0]
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


def draw_attendance_status(img, small_bounding_box, temps):
    bounding_box = [element * 4 for element in small_bounding_box]
    top, right, bottom, left = bounding_box
    w = right-left
    h = bottom-top
    
    text = "Accepted" if temps < 37.5 else "Rejected"
    color = (0,255,0) if temps < 37.5 else (0,0,255)

    # Attendance Status
    img = cv2.rectangle(img, (left, top+int(h/2)+10), (left+150, top+int(h/2)-30), color, cv2.FILLED)
    img = cv2.putText(img, text, (left, top+int(h/2)), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255))
    # Temperature
    img = cv2.putText(img, "Temperature = {}".format(temps), (left, bottom+20), cv2.FONT_HERSHEY_PLAIN, 0.9, (255,255,255), 1)

    return img


def draw_overlay(img):
    curr_time = attendance_window.get_curr_time()
    face_detected = FaceRecognition.face_detection(img)

    if face_detected:
        img = draw_bounding_box(img)

    # Time
    img = cv2.putText(img, curr_time, (0,20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,0))

    return img

if __name__ == "__main__":
    pass