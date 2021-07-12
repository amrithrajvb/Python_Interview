class Collage:
    def setValue(self,name,department,no_course,teachers_count):
        self.name=name
        self.department=department
        self.no_course=no_course
        self.teachers_count = teachers_count
class Bca(Collage):
    def Bvalue(self,students_count):
        self.students_count=students_count
        print("Function Bvalue")
        print("collage name:",self.name)
        print("department",self.department)
        print("teachers count",self.teachers_count)
        print("students count:",self.students_count) #single inheritance

class Mca(Bca):
    def Mvalue(self,no_subjects,course_duration):
        self.no_subjects=no_subjects
        self.course_duration=course_duration
        print("Function Mvalue")
        print("collage name:", self.name)
        print("department", self.department)
        print("no of subjects:",self.no_subjects)
        print("course duration",self.course_duration)# multilevel inheritance
class CsTeacher():
    def Tvalue(self,teacherId,teacherName,teacher_subject):
        print("Function Tvalue")
        self.teacherId=teacherId
        self.teachername=teacherName
        self.teacher_subject =teacher_subject
        print("Teahcher id",self.teacherId)
        print("Teacher name:", self.teachername)
        print("teacher subject", self.teacher_subject)

class Main(Collage,CsTeacher):
    def Avalue(self,principalName,no_ofHod):
        print("Function Avalue")
        self.principalName=principalName
        self.no_ofHod=no_ofHod
        print("principal name:", self.principalName)
        print("no of hod", self.no_ofHod)#multiple inheritance

f=Mca()
z=input("please enter the collage name")
x=input("please enter the department")
y=int(input("enter the no of course"))
w=int(input("enter the teachers count"))
f.setValue(z,x,y,w)
v=int(input("please enter students count"))
f.Bvalue(v)
u=int(input("please enter the no of subjects"))
t=int(input("please enter the course duration"))
f.Mvalue(u,t)
g=Main()
p=int(input("please enter the teacher ID"))
q=input("please enter the teachers anme")
r=input("please enter the teachers_subject")
g.Tvalue(p,q,r)
k=input("please enter the principal name")
l=input("please enter the no of hod")
g.Avalue(k,l)

