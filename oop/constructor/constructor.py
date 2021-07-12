#constructor--to initialize instance variable
## constructor automatically invoke when creating object

class Person:
    def __init__(self,name,age, address):
        self.name=name
        self.age=age
        self.address=address
    def printVal(self):
        print(self.name,self.age,self.address)
na=input("enter the name")
ag=int(input("enter the age"))
ad=input("enter the address")
obj=Person(na,ag,ad)
obj.printVal()

#when we using constructor the program should be precise and we can able to apply the value on at the time of object creation