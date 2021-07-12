class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        print("total:",self.num1+self.num2)
    def multiplication(self):
        print("product:", self.num1 * self.num2)
    def substaction(self):
        print("substraction:", self.num1 - self.num2)
    def division(self):
        print("division",self.num1/self.num2)
a=int(input("please enter the first number"))
b=int(input("please enter the second number"))
obj=Calculator(a,b)
obj.addition()
obj.multiplication()
obj.substaction()
obj.division()


