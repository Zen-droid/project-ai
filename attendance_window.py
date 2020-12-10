from PIL import ImageTk
import PIL.Image as Img
from tkinter import *
import json
import photo_generator
import time

def get_time():
    t = time.localtime()
    curr_time = time.strftime("%H:%M:%S", t)
    return str(curr_time)

def get_employee_data(find_id):
    with open("employee_data.json", "r") as openfile:
        data = json.load(openfile)
        
        return next(item for item in data if item["id"] == find_id)

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

def show_attendance_window(img_path, emp_id):
    root = Tk()
    root.title("Employee Information")

    employee_data = get_employee_data(emp_id)

    if employee_data is None:
        print("Employee data not found!")
        return

    # Import employee image and cropped it into 3:4 aspect ratio 
    img = Img.open(img_path)
    img = photo_generator.photoID_format(img)
    finalImg = ImageTk.PhotoImage(image=img)
    profile_image = Label(root, image=finalImg)
    
    employee_header(root)

    e_id = Label(root, text= str(employee_data["id"]))
    name = Label(root, text= employee_data["name"])
    position = Label(root, text= employee_data["position"])
    division = Label(root, text= employee_data["division"])

    profile_image.grid(row=0, column=0, rowspan=4)
    e_id.grid(row=0, column=3, sticky="w")
    name.grid(row=1, column=3, sticky="w")
    position.grid(row=2, column=3, sticky="w")
    division.grid(row=3, column=3, sticky="w")

    attend_time = Label(root, text="Attendance Time: "+ get_time())
    exit_btn = Button(root, text="Quit", command=root.destroy, background="red")
    attend_time.grid(row=4, column=0, columnspan=4)
    exit_btn.grid(row=5, column=0, columnspan=4)

    root.lift()
    root.attributes("-topmost", True)
    root.mainloop()

if __name__ == "__main__":
    show_attendance_window("data/train/2/001.jpg", 2)
    # data = get_employee_data(5)
    # print(data)
    # print(type(data))
    pass