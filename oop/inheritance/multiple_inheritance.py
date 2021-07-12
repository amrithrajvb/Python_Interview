#multiple inheritance

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child:
    def cvalue(self,address,cls):
        self.address=address
        self.cls=cls
        print(self.address,self.cls)
class Student(Person,Child):
    def svalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
st=Student()
st.pvalue("anju",23)
st.cvalue("akkada",10)
st.svalue(10,230)