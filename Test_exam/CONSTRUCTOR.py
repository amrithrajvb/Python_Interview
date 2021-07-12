class Person:
    company_name="Luminar"
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printValue(self):
        print(self.name,self.age,self.address)
class Employee(Person):
    def __init__(self,id,salary,name,age,address):
        super().__init__(name,age,address)
        self.id=id
        self.salary=salary
        print(self.id,self.salary)
        print(self.name,"salary is",self.salary,"AND COMPANY IS",Person.company_name)

e=Employee(1,200000,"arjun","29","toppilpadi kunnakulam")
e.printValue()
