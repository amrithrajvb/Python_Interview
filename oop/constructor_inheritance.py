#when we use inheritache with constructor we need to add the attaribute list into child
# class constructor's list
#call the base class constuctor using Super() method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("my name is :",self.name)
        print("age is:",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno,self.mark)
s=Student(2,240,"amrith",24)
s.printval()
s.print()


class Vehicle:
    def __init__(self,name,color):
        self.name=name
        self.color=color
class Car(Vehicle):
    def __init__(self,speed,milage,name,color):
        super().__init__(name,color)
        self.speed=speed
        self.milage=milage
        print(self.name,self.color,self.speed,self.milage)
c=Car(100,50,"maruthi","black")


