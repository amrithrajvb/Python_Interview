class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def cvalue(self,salary):
        self.salary=salary
        print(self.salary)
class Parent(Person):
    def prvalue(self,place):
        self.place=place
        print(self.place)
class Employee(Parent):
    def evalue(self,company):
        self.company=company
        print(self.company)
obj=Child()
obj.pvalue("arun",32)
obj.cvalue(3000)
obj2=Employee()
obj2.prvalue("akbb")
obj2.evalue(12000)