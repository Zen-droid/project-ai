import face_recognition
from face_recognition.face_detection_cli import image_files_in_folder
import face_recognition_knn
import cv2
import os
import attendance_window
import overlay


def recognize():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    temperature = 37.9

    while True:
        _, img = cap.read()
        
        img = overlay.draw_overlay(img, temperature)
        cv2.imshow("Face Detection", img)

        # Scaling image down by 1/4 resolution for faster face recognition
        small_img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
        rgb_small_img = cv2.cvtColor(small_img, cv2.COLOR_BGR2RGB)

        face_bounding_boxes = face_recognition.face_locations(rgb_small_img)

        if len(face_bounding_boxes) == 1:
            print("Face Detected")

            predictions = face_recognition_knn.predict(rgb_small_img, model_path="knn_model.clf")
            for name, (top, right, bottom, left) in predictions:
                print("- Found {} at ({}, {})".format(name, left, top))
            
            # if predictions:
            name = predictions[0][0]
            present = attendance_window.check_attendance(name)

            if name != "unknown" and not present:
                status = True if temperature < 37.5 else False
                overlay.draw_attendance_status(img, predictions[0][1], status)
                cv2.imshow("Face Detection", img)

                name_path = os.path.join("data/train", name)
                img_path = image_files_in_folder(name_path)[0]
                attendance_window.show_attendance_window(img_path, name)

            # return predictions[0][0]

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    print("Starting Face Recognition..")
    name = recognize()

