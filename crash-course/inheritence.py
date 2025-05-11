"""class Person:
    def __init__(self, fname:str, lname:str)->None:
        self.firstname = fname 
        self.lastname = lname 
    def printname(self):
        print(self.firstname, self.lastname)"""
        
"""obj = Person("Akib", "Nayan")
obj.printname()"""

"""class Student(Person):
    pass 

obj = Student("Akib", "Nayan")
obj.printname()"""

"""class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        

obj = Student("Akib", "Nayan")
obj.printname()"""

"""class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        
obj = Student("Akib", "Nayan")
obj.printname()"""

"""class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def display(self):
        print(self.firstname, self.lastname, self.graduationyear)

obj = Student("Akib", "Nayan", 2022)
obj.display()"""


class Person:
    def __init__(self, fname:str, lname:str)->None:
        self.firstname = fname
        self.lastname = lname
    def printname(self)->None:
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname:str, lname:str, year:int)->None:
        super().__init__(fname, lname)
        self.graduationyear = year
    def display(self)->None:
        print(self.firstname, self.lastname, self.graduationyear)

obj = Student("Akib", "Nayan", 2022)
obj.display()
print(obj.firstname)
print(obj.lastname)
print(obj.graduationyear)