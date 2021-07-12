class Person:
    def pdetails(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)
class Student(Person):
    def sdeatils(self,rollno,department,mark):
        self.rollno=rollno
        self.department=department
        self.mark=mark
        print(self.rollno,self.department,self.mark)
        print(self.name,"mark is",self.mark)
obj=Student()
obj.pdetails("hari",23,"ackdad")
obj.sdeatils(1,"cs",340)