from face_recognition.face_detection_cli import image_files_in_folder
import face_recognition_knn
import cv2
import os
import attendance_window
import overlay

def face_detection(img):
    cascade_path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 5)

    return True if len(faces) == 1 else False

def recognize():
    cap = cv2.VideoCapture(0)
    temperature = 36.7

    while True:
        _, img = cap.read()
        
        img = overlay.draw_overlay(img)
        cv2.imshow("Face Detection", img)
        face_detected = face_detection(img)

        if face_detected:
            print("Face Detected")
            # Scaling image down by 1/4 resolution for faster face recognition
            small_img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
            rgb_small_img = cv2.cvtColor(small_img, cv2.COLOR_BGR2RGB)

            predictions = face_recognition_knn.predict(rgb_small_img, model_path="knn_model.clf")
            for name, (top, right, bottom, left) in predictions:
                print("- Found {} at ({}, {})".format(name, left, top))
            
            if predictions:
                name = predictions[0][0]
                present = attendance_window.check_attendance(name)

                if name != "unknown" and not present:
                    img = overlay.draw_attendance_status(img, predictions[0][1], temperature)
                    cv2.imshow("Face Detection", img)

                    name_path = os.path.join("data/train", name)
                    img_path = image_files_in_folder(name_path)[0]
                    attendance_window.show_attendance_window(img_path, name, temperature)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    print("Starting Face Recognition..")
    name = recognize()