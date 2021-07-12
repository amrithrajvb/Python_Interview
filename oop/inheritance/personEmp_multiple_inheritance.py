class Person:#parent class, base class,super class
    company_name="Luminar"
    def pdetails(self,name,age):
        self.name=name
        self.age=age

        print(self.name,self.age)
class Child:
    def cvalue(self,address):
        self.address = address
        print(self.address)
class Employee(Person,Child):#child class/derivedclass/sub class
    def edetails(self,id,salary):
        self.id=id
        self.salary=salary
        print(self.id,self.salary)
        print(self.name,"salary is",self.salary)
emp=Employee()
emp.pdetails("anand",23)
emp.cvalue("akkamma")
emp.edetails(10,1222200)