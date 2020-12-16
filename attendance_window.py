from PIL import ImageTk
import PIL.Image as Img
from tkinter import * 
# from tkinter.ttk import *
from datetime import datetime
import db_handler
import photo_generator

class Employee:
    def __init__(self, root, img_path, emp_id):
        self.employee_header(root)
        self.employee_content(root, emp_id)
        self.profile_picture(root, img_path)

    
    def employee_header(self, root):
        self.profile_id = Label(root, text="Employee Id")
        self.profile_name = Label(root, text="Employee Name")
        self.profile_position = Label(root, text="Employee Position")
        self.profile_division = Label(root, text="Employee Division")

        self.profile_id.grid(row=0, column=1, sticky="w")
        self.profile_name.grid(row=1, column=1, sticky="w")
        self.profile_position.grid(row=2, column=1, sticky="w")
        self.profile_division.grid(row=3, column=1, sticky="w")

        for x in range(4):
            self.sep = Label(root, text=":")
            self.sep.grid(row=x, column=2)

    def employee_content(self, root, emp_id):
        self.employee_data = db_handler.get_employee_data(emp_id)[0]

        if self.employee_data is None:
            print("Employee data not found!")
            return

        self.e_id = Label(root, text= self.employee_data[0])
        self.name = Label(root, text= self.employee_data[1])
        self.position = Label(root, text= self.employee_data[2])
        self.division = Label(root, text= self.employee_data[3])

        self.e_id.grid(row=0, column=3, sticky="w")
        self.name.grid(row=1, column=3, sticky="w")
        self.position.grid(row=2, column=3, sticky="w")
        self.division.grid(row=3, column=3, sticky="w")
    
    def profile_picture(self, root, img_path):
        self.img = Img.open(img_path)
        self.img = photo_generator.photoID_format(self.img)
        self.finalImg = ImageTk.PhotoImage(image=self.img)

        self.profile_image = Label(root, image=self.finalImg)
        self.profile_image.grid(row=0, column=0, rowspan=4)  
    
    def attend(self, emp_id):
        emp_data = db_handler.get_employee_data(emp_id)[0]
        data = (emp_data[0], get_curr_time(), "Attended", get_curr_date())

        success = db_handler.insert_attendance_data(data)
        if success:
            print("attendance data success")
        else:
            print("duplicate data")

# style = Style()
# style.configure("btn", font="Calibri", 10, 'Bold')

def get_curr_time():
    curr_time = datetime.now().strftime("%H:%M:%S")
    return str(curr_time)

def get_curr_date():
    curr_date = datetime.now().strftime("%Y-%m-%d")
    return str(curr_date)

def check_attendance(id):
    data = db_handler.get_attendance_data(id)

    if data:
        # Check if attended today
        for dt in data:
            if dt[3] == get_curr_date():
                return True
    return False

def show_attendance_record(root, emp_id):
    record = Toplevel(root)
    record.title("Attendance Record")
    record.geometry("300x200")

    datas = db_handler.get_attendance_data(str(emp_id))

    for x, data in enumerate(datas):
        id = Label(record, text=data[0])
        id.grid(column=0, row=x, columnspan=2)
        time = Label(record, text=data[1])
        time.grid(column=2, row=x, columnspan=2)
        status = Label(record, text=data[2])
        status.grid(column=4, row=x, columnspan=2)


def show_attendance_window(img_path, emp_id):
    root = Tk()
    root.title("Employee Information")

    employee = Employee(root, img_path, emp_id)

    # Import employee image and cropped it into 3:4 aspect ratio

    # employee_header(root)
    # employee_content(root, emp_id)

    attend_time = Label(root, text="Attendance Time: "+ get_curr_time())
    attend_detail = Button(root, text="Attendance Detail", command=lambda: show_attendance_record(root, emp_id), background="#d4d4d4")
    attend_button = Button(root, text="Attend", command=lambda: employee.attend(emp_id), background="#35fc03")
    exit_btn = Button(root, text="Quit", command=root.destroy, background="#fc3503")

    attend_time.grid(row=4, column=0, columnspan=4)
    attend_detail.grid(row=5, column=0, columnspan=1)
    attend_button.grid(row=5, column=1, columnspan=2)
    exit_btn.grid(row=5, column=3, columnspan=2)

    root.lift()
    root.attributes("-topmost", True)
    root.mainloop()

if __name__ == "__main__":
    # show_attendance_window("data/train/2/001.jpg", 2)
    # data = get_employee_data(5)
    # print(data)
    # print(type(data))
    # pass
    # print(check_attendance(5))
    # print(db_handler.get_attendance_data(5))
    db_handler.clear_attendance_record()
    # print(db_handler.get_attendance_data(2))
    # print(check_attendance(5))
    # attend(5)
