# class Person:
#     def pvalue(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.age,self.name)
# class Display(Person):
#     def pvalue(self,salary):
#         self.salary = salary
#         print(self.salary)
# d=Display()
# d.pvalue(1000)


#sample

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.age,self.name)
    def pvalue(self,salary):
        self.salary=salary
        print(self.salary)
p=Person()
p.pvalue(1000000)
