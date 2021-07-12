#only accept one function

def zerodivisor(func):
    def wrapper(num1,num2):
        if (num1==0) | (num2==0):
            raise Exception("invalid parameter")
        return func(num1,num2)
    return wrapper
def decorates_sub(func):
    def wrapper(num1,num2):
        if num1 < num2:
            num1,num2=num2,num1
        return func(num1,num2)
        #     return func(num2,num1)
        # else:
        #     return func(num1,num2)
    return wrapper
@zerodivisor
@decorates_sub
def sub(num1,num2):
    return num1-num2
try:
    n1=int(input("enter the first number"))
    n2=int(input("enter the second number"))
    print(sub(n1,n2))
except Exception as e:
    print(e)