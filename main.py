import sqlite3



# Create the Student table if it doesn't exist
""" con.execute('''CREATE TABLE IF NOT EXISTS Student (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT,
                DEPT TEXT,
                YEAR TEXT
            );''') """

# Rest of your code...


""" con = sqlite3.connect('D:/study files/python/users.db') # connect to database
def insertRecord(name,dept,year):
    query = "insert into Student(NAME,DEPT,YEAR) values (?,?,?);"
    con.execute(query,(name,dept,year)) # execute the query
    con.commit()
    print("Record inserted successfully")

def updateRecord(name,dept,year):
    query = "update Student set DEPT=?,YEAR=? where NAME=?;"
    con.execute(query,(dept,year,name)) # execute the query
    con.commit()
    print("Record updated successfully")

def deleteRecord():
    query = "delete from Student where NAME=?;"
    con.execute(query,(name,))
    con.commit()
    print("Record deleted successfully")

def selectRecord():
    query = "select * from Student;"
    res = con.execute(query)
    con.commit()
    for row in res:
        print(list(row)) """

con = sqlite3.connect('D:/study files/python/users.db') # connect to database
print(dir(con))
def insertRecord(name,dept,exp):
    query = "insert into Staff(NAME,DEPT,EXP) values (?,?,?);"
    con.execute(query,(name,dept,exp)) # execute the query
    con.commit()
    print("Record inserted successfully")

def updateRecord(name,dept,exp,id):
    query = "update Staff set NAME=?,DEPT=?,EXP=? where ID=?;"
    con.execute(query,(name,dept,exp,id)) # execute the query
    con.commit()
    print("Record updated successfully")

def deleteRecord(id):
    query = "delete from Staff where ID=?;"
    con.execute(query,(id,))
    con.commit()
    print("Record deleted successfully")

def selectRecord():
    query = "select * from Staff;"
    res = con.execute(query)
    con.commit()
    for row in res:
        print(list(row))
    


print("""
    1. Insert
    2. Update
    3. Delete
    4. Select
    5. Exit
""")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        dept = input("Enter dept: ")
        exp = input("Enter exp: ")
        insertRecord(name,dept,exp)

    elif choice == 2:
        id = input("Enter ID: ")
        name = input("Enter name: ")
        dept = input("Enter dept: ")
        exp = input("Enter exp: ")
        updateRecord(name,dept,exp,id)

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

