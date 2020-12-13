import sqlite3
import json


# conn = sqlite3.connect("employee_data.db")
# c = conn.cursor()

# c.execute("""
#     CREATE TABLE MsEmployee(
#         EmployeeID INTEGER PRIMARY KEY,
#         Name text NOT NULL,
#         Position text NOT NULL,
#         Division text
#     )
# """)

# c.execute("""
#     CREATE TABLE Attendance(
#         EmployeeID INTEGER,
#         Time text,
#         Status text,
#         Date text,

#         PRIMARY KEY(EmployeeID, Date)
#     )
# """)

# c.execute("DROP TABLE Attendance")

# data_list = []

# with open("employee_data.json") as filereader:
#     data_list = json.load(filereader)

# emp_list = []

# for data in data_list:
#     temp = data["id"], data["name"], data["position"], data["division"]
#     emp_list.append(temp)


# c.executemany("INSERT INTO MsEmployee VALUES(?, ?, ?, ?)", emp_list)


# c.execute("SELECT * FROM MsEmployee")
# data = c.fetchall()

# for n in data:
#     print(n)

# print("Success")
# conn.commit()
# conn.close()

def get_employee_data(id=0):
    conn = sqlite3.connect("employee_data.db")
    c = conn.cursor()

    if id != 0:
        c.execute("SELECT * FROM MsEmployee WHERE EmployeeID=?", str(id))
    else:
        c.execute("SELECT * FROM MsEmployee")
    
    return c.fetchall()

def insert_attendance_data(data):
    conn = sqlite3.connect("employee_data.db")
    c = conn.cursor()
    success = False

    try:
        c.execute("INSERT INTO Attendance VALUES (?,?,?,?)", data)
        success = True
    except sqlite3.IntegrityError:
        success = False
    
    conn.commit()
    conn.close()
    return success

def get_attendance_data(id=0):
    conn = sqlite3.connect("employee_data.db")
    c = conn.cursor()

    if id != 0:
        c.execute("SELECT * FROM Attendance WHERE id=?", str(id))

    c.execute("SELECT * FROM Attendance")
    return c.fetchall()

if __name__ == "__main__":
    data = get_employee_data(2)
    print(data)
    print(type(data))
    # data = get_attendance_data(2)
    # if not data:
    #     print("Empty")
    # else:
    #     for x in data:
    #         print(x)
    
    # data = (5, '13:14:48', 'Attended', '2020-12-14')

    # status = insert_attendance_data(data)

    # if status:
    #     attendance_data = get_attendance_data()
    #     for x in attendance_data:
    #         print(x)
    # else:
    #     print("Duplicate Data")

    print("eof")

