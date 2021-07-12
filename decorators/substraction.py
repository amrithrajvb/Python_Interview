def set(func):
    def wrapper(num1,num2):
        if num1<num2:
            (num1,num2) = (num2,num1)
            return func(num1, num2)#return func(num2,num1)-so won't use swap
        else:
            return func(num1,num2)
    return wrapper

@set
def sub(num1,num2):
    return num1-num2
print(sub(115,10))
@set
def div(num1,num2):
    return num1/num2
print(div(2,10))