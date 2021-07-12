#hierarchial inheritance

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def cvalue(self,address,cls):
        self.address=address
        self.cls=cls
        print(self.address,self.cls)
class Student(Child):
    def setvalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
st=Student()
st.setvalue(10,234)
st.cvalue("addaa",10)
st.pvalue("don",23)