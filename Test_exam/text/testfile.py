class Student:
    def __init__(self,name,rollno,cls,mark):
        self.name=name
        self.rollno=rollno
        self.cls=cls
        self.mark=mark
    def printvalue(self):
            print("name:",self.name)
            print("rollno:",self.rollno)
            print("class:",self.cls)
            print("mark:", self.mark)

    def __str__(self):
        return self.mark
lis=[]
f=open("details",'r')
for line in f:
    words=line.rstrip("\n").split(",")
    name = words[0]
    rollno = words[1]
    cls = words[2]
    mark = words[3]
    obj = Student(name, rollno, cls, mark)
    print(obj)
    obj.printvalue()
    lis.append(obj)## add alltings tom list
print(lis)
mark=[]
for st in lis:
    mark.append(st.mark)
print(mark)#to get mark field only
for st in lis:
    if st.mark==max(mark):
        #print(max(mark))
        print(st.name,st.rollno,st.cls,st.mark)

