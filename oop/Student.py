# class Student():
#     def setValue(self,name,rollno,mark,school):
#         self.name=name
#         self.rollno=rollno
#         self.mark=mark
#         self.school=school
#     def printValue(self):
#         #print(self.name,self.salary,self.company,self.id)if we apply like this we will set the value in setvalue function call
#         print("name :",self.name)
#         print("rollno:",self.rollno)
#         print("mark: ",self.mark)
#         print("school:",self.school)
# a=Student()
# n=input("please eneter the name")
# s=input("please enter the rollno")
# c=input("please enter the mark")
# i=input("please enter the school")
# a.setValue(n,s,c,i)#a.setValue("name",2000,"orion",id)
# a.printValue()
#
# class Student():
#     def setValue(self,name,rollno,mark,school):
#         self.name=name
#         self.rollno=rollno
#         self.mark=mark
#         self.school=school
#         print("name :",self.name)
#         print("rollno:",self.rollno)
#         print("mark: ",self.mark)
#         print("school:",self.school)
# a=Student()
# n=input("please enter the name")
# s=int(input("please enter the rollno"))
# c=int(input("please enter the mark"))
# i=input("please enter the school")
# a.setValue(n,s,c,i)#a.setValue("name",2000,"orion",id)


#using Static

class Students:
    School_name="sjcet pala"
    def setVal(self,name,rollno,div):
        self.name=name
        self.rollno=rollno
        self.div=div
    def printVal(self):
        print("\nname:",self.name, "\n rollno:",self.rollno,"\ndivsion :",self.div,"\nschool name:",Students.School_name)
obj2=Students()
n1=input("please enter the name")
s1=int(input("please enter the rollno"))
c1=int(input("please enter the division"))
obj2.setVal(n1,s1,c1)
obj2.printVal()

