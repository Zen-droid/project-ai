n.predict(original_rgb_img, model_path="knn_model.clf")
            for name, (top, right, bottom, left) in predictions:
                print("- Found {} at ({}, {})".format(name, left, top))

            name = predictions[0][0]
            if name != "unknown":
                name_path = os.path.join("data/train", name)
                img_path = image_files_in_folder(name_path)[0]
                attendance_window.show_at