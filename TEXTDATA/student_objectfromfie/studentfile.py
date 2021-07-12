class Student:
    def __init__(self,name,rollno,cls,mark):
        self.name=name
        self.rollno=rollno
        self.cls=cls
        self.mark=mark
    def printvalue(self):
        print("name:", self.name)
        print("rollno:", self.rollno)
        print("class:", self.cls)
        print("mark:", self.mark)

    def __str__(self):
        return self.name
f=open("student",'r')
for line in f:
    words=line.rstrip("\n").split(",")
    # name=words[0]
    # rollno=words[1]
    # cls=words[2]
    # mark=words[3]
    # obj=Student(name,rollno,cls,mark)
    # print(obj)
    # obj.printvalue()