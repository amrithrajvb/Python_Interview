lis=[10,12,32,43,10,32,26,24,12]
c=[]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):

        if lis[i] ==lis[j]:
            c.append(lis[i])
for i in lis:
    if i in c:
        lis.remove(i)
print("duplicates",c)
print("after remove",lis)






lis=[10,12,32,43,10,32,26,24,12]
lis2=list(set(lis))
print(lis2)
for i in range(len(lis2)):
    for j in range(i+1,len(lis2)):
        if lis2[i] > lis2[j]:
            lis2[i],lis2[j]=lis2[j],lis2[i]

print(lis2)
a=[1,2,3]
b=['a','b','c']
c={}

res = dict(zip(a, b))
print("sdafdsfdsfd",res)

ak=zip(a,b)
d=list(ak)
print(d)
#
#
# for i in a:
#     for j in b:
#            c[j]=i
#            b.remove(j)
#            break
# print(c)


#
# #second
#
# b=[]
# for i in lis:
#     if i not in b:#take all the elements when the repeated value then else will work.
#         b.append(i)
#     else:
#         print("hh",i)

#
lis=[10,12,32,43,10,32,26,24,12]

print(list(set(lis)))

for i in range(len(lis)):
    for j in range(i,len(lis)):
        if lis[i]>lis[j]:
            lis[i],lis[j]=lis[j],lis[i]





print("after reorder",list(set(lis)))



