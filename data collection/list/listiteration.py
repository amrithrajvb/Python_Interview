lis=[1,2,3,4,1,4,"helo",True]
a=[6,9]
lis.extend(a)
print(lis)
# for i in lis:
#     print(i)
# lis.remove(1)
# print(lis)
# lis.clear()
# print(lis)
# del lis
# print(lis)


lis=[1, 0, 5, 2, 6, 0, 6, 8]
c=[]
length=len(lis)
count=0
#[1,5,2,6,6,8,0,0]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):

        if lis[i] ==lis[j]:
            c.append(lis[i])
            lis.extend(c)
            lis.remove(lis[i])
print(lis)
