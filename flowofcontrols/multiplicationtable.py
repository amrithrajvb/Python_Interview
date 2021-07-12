#forloop
num=int(input("enter the number"))
a=1
for a in range(1,11):
    print(a,"*",num,"=",a * num)
    a=a+1

#while
num=int(input("enter the number"))
a=1
while a<= 10:
    res= a * num
    print(a,"*",num,"=",res)
    a += 1