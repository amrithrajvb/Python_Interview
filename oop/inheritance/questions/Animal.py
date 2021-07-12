class Animal:
    def __init__(self,name,type,color):
        self.name=name
        self.type=type
        self.color=color
class Dog(Animal):
    def printvalue(self):
        print("name",self.name)
        print("type:",self.type)
        print("color:",self.color)
obj=Dog("becardi","german","white")
obj.printvalue()
