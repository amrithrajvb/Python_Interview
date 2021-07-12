n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
if n1==n2:
    raise Exception("both numbers are same")
else:
    print(n1+n2)