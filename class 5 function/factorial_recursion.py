# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x*factorial(x-1))
# num=int(input("enter the number"))
# print("the factorial of",num, "is",factorial(num))
#
#
#
#

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

inp=int(input("enter the number"))
print(factorial(inp))

#
# def factorial(x):
#     if x == 1:
#         return 1
#
#     else:
#
#         return (x*factorial(x-1))
#
# inp=int(input("enter the number"))
# print("factorial of",inp,"is:",factorial(inp))