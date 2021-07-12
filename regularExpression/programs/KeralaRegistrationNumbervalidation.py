import re
n=input("enter the registration number")
x="[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}"#KL-[K][L]\d{2}[A-Z]{2}\d{4}
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("Invalid")
