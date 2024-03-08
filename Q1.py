import psycopg
from datetime import datetime
from getpass import getpass

# prints all the students
def getAllStudents():
    cur = db.cursor()
    cur.execute("Select * from students")
    for entry in cur.fetchall():
        print(entry)
    return

# adds a student given the parameters.
def addStudent(first_name, last_name, email, enrollment_date):
    cur = db.cursor()
    valid = True
    try:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES(%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    except:
        valid = False
    if(valid == False):
        print("Add Failed! - cannot have identical emails!")
        # cancel the transaction
        db.rollback()
        return
    db.commit()
    return

#updates a student's email given an id
def updateStudentEmail(student_id, new_email):
    cur = db.cursor()
    valid = True
    try:
        cur.execute("update students set email = %s where student_id=%s", (new_email, student_id))
    except:
        valid = False
    if(valid == False):
        print("Update failed! - cannot have identical emails!")
        # cancel the transaction
        db.rollback()
        return
    db.commit()
    return

#deletes a student based on a given id
def deleteStudent(student_id):
    cur = db.cursor()
    # this %s wants an array instead of an int like the updateStudentEmail function...
    cur.execute("delete from students where student_id=%s", ([student_id]))
    db.commit()
    return

# function which prompts the user to enter the properties of the new student
def getAddStudentArgs():
    while(1):
        fname = input("Enter firstname: ")
        lname = input("Enter lastname: ")
        email = input("Enter email: ")
        date = input("Enter date (YYYY-MM-DD): ")
        #error checking
        if(len(fname)>0 and len(lname)>0 and len(email)>0 and len(date)>0):
            dateformat = "%Y-%m-%d"
            valid = True
            #ensuring the date is in the correct format
            try:
                result = bool(datetime.strptime(date, dateformat))
            except:
                valid = False
            if(valid == True):
                addStudent(fname, lname, email, date)
                return;
            else:
                print("invalid date format.")
        else:
            print("invalid argument(s)!")

# prompts user to enter the id and new email
def getUpdateStudentEmailArgs():
    while(1):
        sid = input("Enter student id: ")
        email = input("Enter new email: ")
        #error checking
        if(len(sid)>0 and len(email)>0):
            if(sid.isdigit() == False):
                print("ID must be an integer.")
                continue
            sid = int(sid)
            updateStudentEmail(sid, email)
            return;
        else:
            print("invalid argument(s)!")

# prompts user to enter the id of the student to be deleted
def getDeleteStudentArgs():
    while(1):
        sid = input("Enter student id: ")
        #error checking
        if(len(sid)>0):
            if(sid.isdigit() == False):
                print("ID must be an integer.")
                continue
            sid = int(sid)
            deleteStudent(sid)
            return;
        else:
            print("invalid argument(s)!")

def main():
    # init some vars
    # display the menu inside infinite loop
    # calls helpers
    while(1):
        print("Enter 1 to getAllStudents\nEnter 2 to addStudent\nEnter 3 to updateStudentEmail\nEnter 4 to deleteStudent\nOther input results in quit.")
        option = input("Enter your option: ")
        if(option == "1"):
            getAllStudents()
        elif(option == "2"):
            getAddStudentArgs()
        elif(option == "3"):
            getUpdateStudentEmailArgs()
        elif(option  == "4"):
            getDeleteStudentArgs()
        else:
            break
    print("exiting program")
    return

#code to connect to the database
dbname=input("Enter database name (default: a3db): ")
user=input("Enter user (postgres): ")
password= getpass("Enter password: ")
inputstr = "dbname="+str(dbname)+" user="+str(user)+" password="+str(password)
db = psycopg.connect(inputstr)
main()
