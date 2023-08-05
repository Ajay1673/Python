""" name1 = hi hello ajay, welcome to mithrasoft hi hello ajay, welcome to mithrasoft
hi hello ajay, welcome to mithrasofthi hello ajay, welcome to mithrasoft
hi hello ajay, welcome to mithrasofthi hello ajay, welcome to mithrasoft
hi hello ajay, welcome to mithrasofthi hello ajay, welcome to mithrasoft
print(name1)

#lists.......................................................

para = ["Ajay","Rathnam","G"]
s = "ajay"
print(s[4::-1])

arr = map(int,input().split(' '))
print(arr)
extend function also in list.................
arr1 = [10,20,30,10,40,10,20]
i=0
while i<len(arr1):
    if(arr1[i]==10):
        arr1.remove(arr1[i])
    i+=1
        
print(arr1)
#..................................................................
#tuples

a = (1,2,3,4,5,6,7)
b=(9,8,7,6,5)
c = a+b
print(c)
a=(10,)*5
print(a)

#....................................................................
#sets...............

a = {1,2,3,4}
b = {'a',2,'b',4,'c',6,'d'}
a.intersection_update(b)
print(a)
"""
#.................................................................
#dictionary...........
""" a={'a':{'c':2,
   'd':4},
   'b':3,
  }
print(a['a']['c']) """

#..................................................................

#datetime

""" import datetime as dt
today = dt.date.today()
time = dt.datetime.now()
print(today)
print(time) 
newyear = dt.datetime(2024,1,1)
print(newyear.date())

remdays = newyear - time
print(remdays) """

#............................................................

#Exceptions

""" try:
    a = 5/0
except Exception as e: #executes if any exception arises
    print(e)
else: #executes if no exception
    print(a)
finally: #executes even if there is an exception or not
    print("bye") """

#Type of Exceptions in Python...........

""" print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

try:
    a = [10,20,30]
    print(a[5])
except IndexError as e:
    print(e)
    print("Invalid Index") #custom message

try:
    f=open("ajay.txt") #if file name wrong or file doesn't exist throws error
except FileNotFoundError:
    print("File Not Found")
else:
    print("f.read()")

try:
    a = int("Joes")
except ValueError as e:
    print(e) """

#Multiple Exception Handling

""" try:
    a = 10/0
    print(a)
    b = int("ajay")
    print(b)
    c = [10,20,30]
    print(c[10])
except ZeroDivisionError:
    print("Zero")
except ValueError:
    print("Invalid casting")
except IndexError:
    print("Invalid index") """

#............................................................

#OOPS
""" class Car():
    pass

swift = Car()
print(isinstance(swift,Car))
print(type(swift)) """

import datetime as dt

""" class Hero():
    today = dt.date.today()
    name = "Ajay"
    year = 2003
    gender = "male"
    def __init__(self,name,year):
        self.name = name
        self.year = year
    
    def printAge(self,year):
        print(self.name+"'s age is:",Hero.today.year - year) """


""" today = dt.date.today()
class Hero():
    def __init__(self,name,year):
        self.current = today.year
        self.name = name
        self.year = year
    @property
    def printAge(self):
        print(self.name+"'s age is:",self.current - self.year) """

#getattr method
#print(getattr(Hero,'name'))
#dot notation
#print(Hero.age)
#print(getattr(Hero,'designation'))#attribute error
#setattr(Hero,'name','Rathnam')
#print(getattr(Hero,'name'))
#Hero.name = "Ajay Rathnam"
#print(Hero.name)
#delattr(Hero,'age') / del Hero.age
# obj = Hero('Krishna')

#obj = Hero('Krishna',2005)
#print(obj.printAge)
#obj.year = 2003
#print(obj.printAge)
#Hero.printAge()
#obj.printAge()
#Hero.printAge(obj,2004)
#obj.printAge(2004)
#obj.gender = "Male"
#print(Hero.__dict__)
#print(obj.__dict__)
#obj.printAge(2005)

#getter/setter in decorators


""" today = dt.date.today()
class Hero():
    def __init__(self,name,year):
        self._current = today.year
        self._name = name
        self._year = year
    @property
    def printAge(self):
        print(self._name+"'s age is:",self._current - self._year)

    def getAge(self):
        return self._year
    
    def setAge(self,year):
        self._year = year
        return True
    
obj = Hero("ajay",2003)
obj.setAge(24)
#print(obj.year)
print(obj.getAge())
print(Hero.__dict__)
print(obj.__dict__) """

#....................................................

""" today = dt.date.today()
class Hero():
    def __init__(self,name,year):
        self._current = today.year
        self._name = name
        self._year = year
    @property
    def printAge(self):
        print(self._name+"'s age is:",self._current - self._year)

    @property
    def getAge(self):
        return self._year
    
    @getAge.setter
    def getAge(self,year):
        self._year = year
        return True
    
obj = Hero("ajay",2003)
obj.getAge = 24
#print(obj.year)
print(obj.getAge)
print(Hero.__dict__)
print(obj.__dict__) """

""" today = dt.date.today()
class Hero():
    def __init__(self,name,year):
        self._current = today.year
        self._name = name
        self._year = year

    def getter(self):
        return self._year
    
    def setter(self,year):
        self._year = year
        return True
    
    year = property(getter,setter)
    
obj = Hero("ajay",2003)
print(obj.year)
obj.year = 24
#print(obj.year)
print(obj.year)
#print(Hero.__dict__)
#print(obj.__dict__) """



#class method decorator
""" class Employee():
    count=0
    @classmethod #class method decorator 
    @property
    def enrollNumber(cls):
        return cls.count

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count+=1

    @property
    def printDetails(self):
        Employee.welcome()
        print(self.name+"getting",self.salary,"per annum.")
        

    @staticmethod #static method decorator
    def welcome():
        print("Welcome to TCS Family")

obj1 = Employee('Hari',700000)
obj2 = Employee('Praveen',650000)

print(obj1.enrollNumber)
print(obj2.enrollNumber)
obj1.printDetails """

#Abstraction & Encapsulation

""" class Book:
    def __init__(self,books):
        self.books=books

    def list_books(self):
        print('List of Books: ')
        for book in self.books:
            print(book)
        print('')

    def borrow(self,bookname):
        if bookname in self.books:
            print('Book borrowed',end="\n")
            self.books.remove(bookname)
        else:
            print('Book not available')

    def returnBook(self,bookname):
        print("Book Returned!",end="\n")
        self.books.append(bookname)

booklist = Book(['narnia','marvel','thermodynamics','C++','data structures in c',"APJ's India2020"])
booklist.list_books()
while True:
    print("1. Display
    2. Borrow
    3. Return")
    ch = int(input("Enter your choice : "))
    if(ch==1):
        o.list_books()
    elif(ch==1):
        book = input("Enter book name : ")
        o.borrow(book)
    elif ch==3:
        book = input("Enter book name : ")
        o.returnBook(book)
    else:
        quit()


booklist.borrow('narnia')
booklist.list_books()
booklist.returnBook('narnia')
booklist.list_books() """


#Inheritance
#single inheritance
""" class Yamaha:
    company = "Yamaha"
    def bikedetail(self):
        print("Engine CC : 150cc")

class Rseries(Yamaha):
    def __init__(self,name,year,type):
        self.name = name
        self.year = year
        self.type = type
    
    def bikeinfo(self):
        print("Company : "+self.company,
              "\nType : "+self.type,
              "\nName : "+self.name,
              "\nModel : "+self.year)
        
R15 = Rseries('R15 v3','2019','Sport')
R15.bikeinfo()
R15.bikedetail() """

#multiple inheritance
""" class Yamaha:
    company = "Yamaha"
    def bikedetail(self):
        print("Engine CC : 150cc")

class Bajaj:
    company = "Bajaj"
    def bikedetail(self):
        print("Engine CC : 200cc")

class Rseries(Yamaha,Bajaj): # it takes from the base class based on order. It sees which cls name came first and inherits that base class. So it inherits from yamaha
    def __init__(self,name,year,type):
        self.name = name
        self.year = year
        self.type = type
    
    def bikeinfo(self):
        print("Company : "+self.company,
              "\nType : "+self.type,
              "\nName : "+self.name,
              "\nModel : "+self.year)
        
R15 = Rseries('R15 v3','2019','Sport')
R15.bikeinfo()
R15.bikedetail() """

#methoad overriding 
#diamond problem
""" class A:
    def printInfo(self):
        print("Hi")
    #pass
class B(A):
    def printInfo(self):
        print("Hello")
    #pass
class C(A):
    def printInfo(self):
        print("Hey")
    #pass
class D(B,C):
    #pass
    def printInfo(self):
        print('Bye')

obj = D()
obj.printInfo()

#operator overloading
class Number:
    def __init__(self,value):
        self.value = value

    def __add__(obj1,obj2):
        return obj1.value + obj2.value
     
obj1 = Number(5)
obj2 = Number(10)
print(obj1+obj2) """

""" + - __add__
- - __sub__
* - __mul__
/ - __trueDiv__
// - __floordiv__
% - __mod__
** - __pow__
& - __and__
| - __or__
^ - __xor__

< - __LT__ 
> - __GT__
<= - __LE__
== - __EQ__
!= - __NE__
>= - __GE__

<< - __lshift__
>> - __rshift__
+= - __iadd__
-= - __isub__
*= - __imul__
/= - __idiv__ """

#Abstract class
""" from abc import ABC,abstractmethod #library for abstract class
class Bank(ABC): #inherited from abstract class ABC
    @abstractmethod
    def debit(self):
        pass
    @abstractmethod
    def credit(self):
        pass

class TMB(Bank):
    def debit(self):
        print("Debited")
    def credit(self):
        print("Credited")

obj = TMB()
#obj1 = Bank()

obj.debit()
#obj1.debit() """

#Function Overriding
""" class Employee:
    def Workhrs(self):
        self.hrs = 50
    def printhrs(self):
        print(self.hrs)
    
class Trainee(Employee):
    def Workhrs(self):
        self.hrs = 60

    def resetHrs(self):
        super().Workhrs()

emp = Employee()
emp.Workhrs()
emp.printhrs()
 
trainee = Trainee()
trainee.resetHrs()
trainee.printhrs() """

#File Handling..............................
""" file = open("C:/Users/AVITA/Desktop/IOT_project.txt","r")
# print(file.read())
# file.close()
# print(file.readline())
# print(file.readline(2))
#print(file.readlines()) #It converts each line into list values
for line in file: #print line by line
    print(line)
file.close()"""


""" 
import os
file = open("C:/Users/AVITA/Desktop/IOT.txt","w")
file.write("Hi Guys")
file.close() """

""" file = open("C:/Users/AVITA/Desktop/IOT.txt","a")
file.write("\nHey Girl")
file.close()

file = open("C:/Users/AVITA/Desktop/IOT.txt","r")
print(file.read())
file.close()

if os.path.exists("C:/Users/AVITA/Desktop/IOT.txt"):
    os.remove("C:/Users/AVITA/Desktop/IOT.txt")
    #os.rmdir("folder name")
else:
    print("File not Found") """

import solar_system as sys
var = sys.create()
print(var)

