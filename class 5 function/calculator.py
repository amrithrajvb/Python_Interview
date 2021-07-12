def add(a,b):
    return int(a + b)
def sub(a,b):
    return a - b
def mult(a,b):
    return int(a * b)
def div(a,b):
    return a /b
print("select operation")
print("1.ADD")
print("2.substraction")
print("3.multiplication")
print("4.division")
while True:
    choice = int(input("enter the choice"))
    #choice = input("enter the choice")
    if choice in (1, 2, 3, 4):
    #if choice in("1","2","3","4"):
        num1= float(input("enter the number1"))
        num2 = float(input("enter the number2"))
        #if choice == '1'-likewise
        if choice == 1:
            print(add(num1,num2))
        elif choice == 2:
            print(sub(num1,num2))
        elif choice == 3:
            print(mult(num1,num2))
        elif choice == 4:
            print(div(num1,num2))
        break
    else:
        print("invalid")
