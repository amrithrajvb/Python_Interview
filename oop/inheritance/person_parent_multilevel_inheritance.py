class Person:#parent class, base class,super class
    company_name="Luminar"
    def pdetails(self,name,age):
        self.name=name
        self.age=age

        print(self.name,self.age)
class Parent(Person):
    def pvalue(self,address):
        self.address = address
        print(self.address)

class Employee(Parent):#child class/derivedclass/sub class
    def edetails(self,id,salary):
        self.id=id
        self.salary=salary
        print(self.id,self.salary)
        print(Person.company_name,"of",self.name,"salary is",self.salary)
emp=Employee()
emp.pdetails("arjun",23)
emp.pvalue("akkada")
emp.edetails(101,210000)

#if we using the parent class attribute in chid class first call the parent class method then accordingly
