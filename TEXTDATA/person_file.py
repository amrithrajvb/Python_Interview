class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print("name", self.name)
        print("age",self.age)

    def __str__(self):
            return self.name
f = open("person", 'r')
# print(f)
for i in f:
    words = i.rstrip("\n").split(",")
    # print(words)
    name=words[0]
    age=words[1]
    obj=Person(name,age)
    print(obj)
    obj.print()












            # words = i.split(" ")
            # # words=i.rstrip('\n').split(" ")-rstrip used for removing particular element
            # for j in words:
            #     print(j)
            #     # self.count=j
            #     # print(self.count)
            #     break





