from tabulate import tabulate
import mysql.connector as db

con = db.connect(host="localhost",user="root",password="ajayKrishna03",database="users")

# print(dir(con))

if con:
    print("Connection Established")
else:
    print("Error")

res = con.cursor()
def insertRecord(name,dept,year):
    query = "insert into Student(NAME,DEPT,YEAR) values (%s,%s,%s);"
    res.execute(query,(name,dept,year)) # execute the query
    con.commit()
    print("Record inserted successfully")

def updateRecord(name,dept,year,id):
    query = "update Student set NAME=%s,DEPT=%s,YEAR=%s where ID=%s;"
    res.execute(query,(name,dept,year,id)) # execute the query
    con.commit()
    print("Record updated successfully")

def deleteRecord(id):
    query = "delete from Student where ID=%s;"
    res.execute(query,(id,))
    con.commit()
    print("Record deleted successfully")

def selectRecord():
    query = "select * from Student;"
    res.execute(query)
    result = res.fetchall()
    # result = res.fetchone()
    # result = res.fetchmany()
    con.commit()
    print(tabulate(result,headers=['ID','Student Name','Department Name','Year of Studying']))

    
    


print("""
    1. Insert
    2. Update
    3. Delete
    4. Select
    5. Exit
"""
)

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        dept = input("Enter dept: ")
        year = input("Enter year: ")
        insertRecord(name,dept,year)

    elif choice == 2:
        id = input("Enter ID: ")
        name = input("Enter name: ")
        dept = input("Enter dept: ")
        year = input("Enter year: ")
        updateRecord(name,dept,year,id)

    elif choice == 3:
        id = input("Enter ID: ")
        deleteRecord(id)

    elif choice == 4:
        selectRecord()

    elif choice == 5:
        print("Thank you")
        con.close() # close the connection
        quit()

    else:
        print("Invalid choice")