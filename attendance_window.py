from PIL import ImageTk
import PIL.Image as Img
from tkinter import *
# from tkinter.ttk import *
from datetime import datetime
import db_handler
import photo_generator

class Table:
    def __init__(self, root, rows, datas):
        # Header
        self.header = ["Employee ID", "Time", "Attendance", "Date"]
        for i in range(4):
            self.e = Entry(root, width=15, fg="blue", font=("Arial", 9, "bold"))
            self.e.grid(row=0, column=i)
            self.e.insert(END, self.header[i])

        # Content
        for i in range(rows):
            for j in range(4):
                self.e = Entry(root, width=15, fg="black", font=("Arial", 9, "bold"))
                self.e.grid(row=i+1, column=j)
                self.e.insert(END, datas[i][j])


class Employee:
    def __init__(self, root, img_path, emp_id):
        self.employee_header(root)
        self.employee_content(root, emp_id)
        self.profile_picture(root, img_path)
    
    def employee_header(self, root):
        self.header = ["Employee Id", "Employee Name", "Employee Position", "Employee Division"]

        for i in range(4):
            self.e = Label(root, text=self.header[i])
            self.e.grid(row=i, column=1, sticky="w")

            self.sep = Label(root, text=":")
            self.sep.grid(row=i, column=2)

    def employee_content(self, root, emp_id):
        self.employee_data = db_handler.get_employee_data(emp_id)[0]

        if self.employee_data is None:
            print("Employee data not found!")
            return

        for i in range(4):
            self.e = Label(root, text=self.employee_data[i])
            self.e.grid(row=i, column=3, sticky="w")

        self.attend_time = Label(root, text="Attendance Time: "+ get_curr_time())
        self.attend_detail = Button(root, text="Attendance Detail", command=lambda: self.show_attendance_record(root, emp_id), background="#d4d4d4")
        self.exit_btn = Button(root, text="Quit", command=root.destroy, background="#fc3503")

        self.attend_time.grid(row=4, column=0, columnspan=4)
        self.attend_detail.grid(row=5, column=0, columnspan=1)
        self.exit_btn.grid(row=5, column=1, columnspan=2)
    
    def profile_picture(self, root, img_path):
        self.img = Img.open(img_path)
        self.img = photo_generator.photoID_format(self.img)
        self.finalImg = ImageTk.PhotoImage(image=self.img)

        self.profile_image = Label(root, image=self.finalImg)
        self.profile_image.grid(row=0, column=0, rowspan=4)  
    
    def attend(self, emp_id, attend_status):
        emp_data = db_handler.get_employee_data(emp_id)[0]
        data = (emp_data[0], get_curr_time(), attend_status, get_curr_date())

        success = db_handler.insert_attendance_data(data)
        if success:
            print("attendance data success")
        else:
            print("duplicate data")
    
    def show_attendance_record(self, root, emp_id):
        self.record = Toplevel(root)
        self.record.title("Attendance Record")
        self.record.geometry("400x200")

        datas = db_handler.get_attendance_data(emp_id)
        print(datas)
        print(len(datas))

        self.output = Table(self.record, len(datas), datas)


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

def show_attendance_window(img_path, emp_id, temps):
    root = Tk()
    root.title("Employee Information")

    employee = Employee(root, img_path, emp_id)

    status = "Attended" if temps < 37.5 else "Absent"
    employee.attend(emp_id, status)

    root.lift()
    root.attributes("-topmost", True)
    root.mainloop()

if __name__ == "__main__":
    pass
