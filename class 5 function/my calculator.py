print("select operation")
print("1.ADD")
print("2.substraction")
print("3.multiplication")
print("4.division")
choice= int(input("enter the choice"))
for i in range(choice):
    if choice == 1:
        def add():
            num1 = int(input("enter the number"))
            num2 = int(input("enter the number"))
            print(num1 + num2)
        add()
    elif choice == 2:
        def sub():
            num1 = int(input("enter the number"))
            num2 = int(input("enter the number"))
            print(num1 - num2)
        sub()
    elif choice == 3:
        def mult():
            num1 = int(input("enter the number"))
            num2 = int(input("enter the number"))
            print(num1 * num2)
        mult()
    elif choice == 4:
        def div():
            num1 = int(input("enter the number"))
            num2 = int(input("enter the number"))
            print(num1 + num2)
        div()
    continue #lhe loop again if we provide break then break the loop
else:
    print("invalid")
