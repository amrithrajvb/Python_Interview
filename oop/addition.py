# class Addition():
#     def setValue(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def printValue(self,sum):
#         self.sum=sum
#         print("sum=",sum)
# p=Addition()
# a=int(input("please enter the first element"))
# b=int(input("please enter the second element"))
# c=a+b
# p.setValue(a,b)
# p.printValue(c)

# class Addition():
#     def setValue(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         #print("sum=", self.num1 + self.num2)#we need only callsetvalue
#     def printValue(self,):
#         print("sum=",self.num1+self.num2)
# p=Addition()
# a=int(input("please enter the first element"))
# b=int(input("please enter the second element"))
# p.setValue(a,b)
# p.printValue()


















class Addition:
    def setValue(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def printValue(self):
        print("sum:",self.num1+self.num2)
ad=Addition()
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
ad.setValue(n1,n2)
ad.printValue()

