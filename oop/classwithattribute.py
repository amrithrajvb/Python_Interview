# class Person:
#     def setval(self,name,age):
#         self.name=name #instance variable
#         self.age=age
#     def printval(self):
#         print("name:",self.name)
#         print("age:",self.age)
# pe=Person()
# na=input("enter the name")
# ag=input("enter the age")
# pe.setval(na,ag)
# pe.printval()
#

#employee

class Employee():
    def setValue(self,name,salary,company,id):
        self.name=name
        self.salary=salary
        self.company=company
        self.id=id
    def printValue(self):
        #print(self.name,self.salary,self.company,self.id)if we apply like this we will set the value in setvalue function call
        print("name :",self.name)
        print("salary:",self.salary)
        print("company: ",self.company)
        print("id:",self.id)
a=Employee()
n=input("please eneter the name")
s=input("please enter the salary")
c=input("please enter the company")
i=input("please enter the id")
a.setValue(n,s,c,i)#a.setValue("name",2000,"orion",id)
a.printValue()

#we have to create multiple object

# a1=Employee()
# n1=input("please eneter the name")
# s1=input("please enter the salary")
# c1=input("please enter the company")
# i1=input("please enter the id")
# a1.setValue(n1,s1,c1,i1)#a.setValue("name",2000,"orion",id)
# a1.printValue()