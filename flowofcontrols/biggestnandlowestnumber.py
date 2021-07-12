# num1=int(input("enter the first number "))
# num2=int(input("enter the second number"))
# if num1 > num2:
#     print("greatest number is",num1)
# elif num2 > num1:
#     print("greatest number is",num2)
# else:
#     print("both are equal")

# 3 number
# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))
# num3 = int(input("enter the third number"))
# if num1 > num2:
#     print(num1,"is greater")
# elif num2 > num3:
#     print(num2,"is greater")
#
# elif num3 > num1:
#     print(num3, "is greater")
#
# else:
#     print("both are equal")

# better way
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))
if (num1 > num2)&(num1 > num3):
    print("num1 is max")

elif (num2 > num1)&(num2 > num3):
    print("num2 is greater")
else:
    print("num3 is max")

