from PIL import ImageTk
import PIL.Image as Img
from tkinter import *
from datetime import datetime
import db_handler
import photo_generator


def get_curr_time():
    curr_time = datetime.now().strftime("%H:%M:%S")
    return str(curr_time)

def get_curr_date():
    curr_date = datetime.now().strftime("%Y-%m-%d")
    return str(curr_date)

def employee_header(root):
    profile_id = Label(root, text="Employee Id")
    profile_name = Label(root, text="Employee Name")
    profile_position = Label(root, text="Employee Position")
    profile_division = Label(root, text="Employee Division")

    profile_id.grid(row=0, column=1, sticky="w")
    profile_name.grid(row=1, column=1, sticky="w")
    profile_position.grid(row=2, column=1, sticky="w")
    profile_division.grid(row=3, column=1, sticky="w")

    for x in range(4):
        sep = Label(root, text=":")
        sep.grid(row=x, column=2)

def employee_content(root, img_path, emp_id):
    # Import employee image and cropped it into 3:4 aspect ratio 

    employee_data = db_handler.get_employee_data(emp_id)

    if employee_data is None:
        print("Employee data not found!")
        return

    e_id = Label(root, text= str(employee_data[0][0]))
    name = Label(root, text= employee_data[0][1])
    position = Label(root, text= employee_data[0][2])
    division = Label(root, text= employee_data[0][3])


    e_id.grid(row=0, column=3, sticky="w")
    name.grid(row=1, column=3, sticky="w")
    position.grid(row=2, column=3, sticky="w")
    division.grid(row=3, column=3, sticky="w")

def attend(id):
    emp_id = db_handler.get_employee_data(id)[0][0]
    data = (emp_id, get_curr_time(), "Attended", get_curr_date())

    success = db_handler.insert_attendance_data(data)
    if success:
        print("attendance data success")
    else:
        print("duplicate data")


def show_attendance_window(img_path, emp_id):
    root = Tk()
    root.title("Employee Information")

    img = Img.open(img_path)
    img = photo_generator.photoID_format(img)
    finalImg = ImageTk.PhotoImage(image=img)
    profile_image = Label(root, image=finalImg)
    profile_image.grid(row=0, column=0, rowspan=4)
    
    employee_header(root)
    employee_content(root, img_path, emp_id)

    attend_time = Label(root, text="Attendance Time: "+ get_curr_date() + " " + get_curr_time())
    attend_button = Button(root, text="Attend", command=attend(emp_id))
    exit_btn = Button(root, text="Quit", command=root.destroy, background="red")

    attend_time.grid(row=4, column=0, columnspan=4)
    attend_button.grid(row=5, column=0, columnspan=2)
    exit_btn.grid(row=5, column=1, columnspan=2)

    root.lift()
    root.attributes("-topmost", True)
    root.mainloop()

if __name__ == "__main__":
    show_attendance_window("data/train/2/001.jpg", 2)
    # data = get_employee_data(5)
    # print(data)
    # print(type(data))
    # pass