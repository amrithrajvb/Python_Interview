class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("my name is :",self.name)
        print("age is:",self.age)
class Employee(Person):
    def __init__(self,salary,empid,name,age):
        super().__init__(name,age)
        self.salary=salary
        self.empid=empid
    def print(self):
        print(self.salary,self.empid)
e=Employee(20000,12,"ARJUN",29)
e.printval()
e.print()
