import  re
n=input("enter the string")
x="[A-Z]{1}[a-z0-9\W]+"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")