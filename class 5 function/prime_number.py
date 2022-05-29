#2,3,5,7,11,13

num1= int(input("enter the number"))
if num1 > 1:
    for i in range(2, num1):
        if (num1 % i) == 0:
             print("number is not prime")
             break
    else:

        print("number is prime")
else:
    print("please entet the positive nmber")