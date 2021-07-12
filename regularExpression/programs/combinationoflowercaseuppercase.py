import re
n=input("enter the elements")

x="[a-zA-Z]+\d{1}$"#x="\w+\d{1}$"we need one combination
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")