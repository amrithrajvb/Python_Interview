import re
n=input("enter the number")
x="[+][9][1]\d{10}$"#x=\d{10}
match=re.fullmatch(x,n)
if match is not None:
    print("Valid-indian number")
else:
    print("invalid")