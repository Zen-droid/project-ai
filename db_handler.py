import sqlite3

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

def get_attendance_data(id):
    conn = sqlite3.connect("employee_data.db")
    c = conn.cursor()

    c.execute("SELECT * FROM Attendance WHERE EmployeeID=?", str(id))

    # c.execute("SELECT * FROM Attendance")
    return c.fetchall()

if __name__ == "__main__":
    data = get_employee_data(2)
    pass

