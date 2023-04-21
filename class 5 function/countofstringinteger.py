# a="athira123kv"
# n="1234567890"
#
# print(n)
# c=""
# d=""
# count=0
# countn=0
# for i in a:
#     if i not in n:
#         c=c+i
#         count=count+1
#     elif n not in a:
#         d=d+i
#         countn=countn+1
# print(c,count)
# print(d,countn)
#
#
# s="athira12378kv"
# n="1234567890"
# count=0
# countn=0
# c=[]
# d=[]
# for i in s:
#     if i in n:
#         countn+=1
#         c.append(i)
#     else:
#         d.append(i)
#         count+=1
# print(c,countn)
# print(d,count)
# #
# #
# # ##
# # s="athira123kv"
# # n="1234567890"
# # count=0
# # countn=0
# # for i in s:
# #     if i in n:
# #         countn=countn+1
# #     else:
# #         count=count+1
# # print(count)
# # print(countn)
#
#
def abc(menu=[]):
    menu.append("soc")
    return menu
print(abc())
print(abc())
print(abc())
#
# from math import sqrt
#
#
# a=[x for x in range(101)  if x > 1 if all ((x% j !=0) for j in range(2,x)) ]
# print(a)
#
#
#
#
s="athira12378kvmanudsfsdgsdgsdgsdmanu"
n="man"
count=0
for i in range(len(s)):
    if s[i]==n[0]:
        if s[i+1] == n[1]:
            if s[i+2] == n[2]:
                count=count+1
print(count)
#
#
# c=[c for c in range(101) if c > 1 if all((c%j !=0 for j in range(2,c)))]
# print(c)
#
#
#
#
#
#
#
#
#
# abc="123"[::-1]
# print(abc)


c=1234

temp=c
sum=0
while temp >0:
    d=temp%10
    print(d)
    sum=sum*10+d
    temp=temp //10
print(sum)