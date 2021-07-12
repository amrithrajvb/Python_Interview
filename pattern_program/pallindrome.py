# # a="Luminar"
# # print(a[::-1])#concept from list
# inp=input("enter the string")
# k=""
# k=k + inp[::-1]
# if k == inp:
#     print("pallindrome")
# else:
#     print("not pallindrome")

#number(convert to string)

num=int(input("entrer the number"))
b=str(num)
c=b[::-1]
print(c)
if c == b:
    print("pallindrome")
else:
    print("not pallindrome")

# for i in range(num[0],num[num]):
#     print(num[num])

#pallindrom number:
# no=int(input(" enter the number"))
# rev=0
# while(no!=0):
#     digit=no%10 #remainder
#     rev=rev*10+digit
#     no=no//10
# print(rev)
# if rev ==no:
#     print("pallindrome")
# else:
#     print("not pallindrome")