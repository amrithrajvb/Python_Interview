# f1=open("wordcounttext",'r')
# f1=""
# dic={}
# for i in f1:
#     words=i.rstrip("\n").split(" ")
#     #words=i.rstrip('\n').split(" ")-rstrip used for removing particular element
#     for j in words:
#         count=words.count(j)
#         dic.update({j:count})
# print(dic)

#


d={}
lmt=int(input("enter the limit"))
for i in range(lmt):
    inp = input("enter the key")
    inp2 = input("enter the value")

    d[inp] = inp2
inps = input("enter the element")
for key,value in d.items():
    if inps == key:
        print(value)
print(d)











#
# f1=open("test","r")
# dic={}
# for i in f1:
#     words=i.rstrip("\n").split(",")
#     for j in words:
#         count=words.count(j)
#         dic.update({j:count})
# print(dic)

k=input("enter the string")
v={}
words =k.split(" ")
for i in words:
    count = words.count(i)
    v.update({i:count})

    # print(words)
    # for j in words:
    #     print("sadsd",j)
    #     count=words.count(j)
    #     v.update({j:count})
print(v)