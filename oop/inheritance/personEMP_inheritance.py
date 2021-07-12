#single inheritance
class Person:#parent class, base class,super class
    company_name="Luminar"
    def pdetails(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)
class Employee(Person):#child class/derivedclass/sub class
    def edetails(self,id,salary):
        self.id=id
        self.salary=salary
        print(self.id,self.salary)
        print(self.name,"salary is",self.salary,Person.company_name)
obj=Employee()
obj.pdetails("aravind",20,"akkada")
obj.edetails(101,122000)