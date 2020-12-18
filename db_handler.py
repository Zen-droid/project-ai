import sqlite3

def get_employee_data(id=0):
    conn = sqlite3.connect("employee_data.db")
    c = conn.cursor()

    if id != 0:
        c.execute("SELECT * FROM MsEmployee WHERE EmployeeID=?", (id,))
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
        c.execute("SELECT * FROM Attendance WHERE EmployeeID=?", (id,))
    else:
        c.execute("SELECT * FROM Attendance")
    return c.fetchall()

def clear_attendance_record(id=0):
    conn = sqlite3.connect("employee_data.db")
    c = conn.cursor()

    if id != 0:
        c.execute("DELETE FROM Attendance WHERE EmployeeID=?", str(id))
    else:
        c.execute("DELETE FROM Attendance")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    pass

