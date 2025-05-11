class Animal:
    name = "dog"
    color = 'brown'
    
obj1 = Animal()

class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def display(self):
        return f"My name is {self.name} and I'm {self.age} years old"
    
obj = Person("Akib", 24)
print(obj.display())