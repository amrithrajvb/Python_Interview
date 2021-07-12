class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print("person method",self.age,self.name)
class Child(Person):
    def pvalue(self,clas):
        self.clas=clas
        print("child method",self.clas)
c=Child()
c.pvalue("abc")

#child class method inherit parent class method