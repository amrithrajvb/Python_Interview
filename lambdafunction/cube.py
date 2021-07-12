inp=int(input("please enter the number"))
print(inp,"quebe is:",inp**3)

def cube(num):
    return  num**3
print(cube(2))

#lambda function

a=lambda num:num**3
print(a(5))
print(a(7))

#multiple elements

a=lambda num,num2:num**3+num2**3
print(a(5,7))

a=lambda num,num2:num+num2
print(a(5,7))
print(a(7,10))


#using user input
a=lambda num,num2:num+num2
b=int(input("enter the first number"))
c=int(input("enter the second number"))
print(a(b,c))

