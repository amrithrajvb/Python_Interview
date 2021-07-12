class Teacher:
    school_name="Asm hss"
    #tid=1
    def __init__(self,tid,tname,subject,department):
        self.tid=tid
        self.tname=tname
        self.subject=subject
        self.department=department
    def printVal(self):
        print("teacher id:",self.tid)
        print("teachername",self.tname)
        print("subject", self.subject)
        print("department", self.department)
        print("school name:",Teacher.school_name)
a1=int(input("enter the teacher id"))
a=input("enter the teacher name")
b=input("enter the subject")
c=input("enter the department")
obj=Teacher(a1,a,b,c)
obj.printVal()


