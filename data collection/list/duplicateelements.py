lis=[10,12,32,43,10,32,26,24,12]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        print(lis[j])
        if lis[i] ==lis[j]:
            print("dupliczte",lis[i])




a=[1,2,3]
b=['a','b','c']
c={}

res = dict(zip(a, b))
print("sdafdsfdsfd",res)

ak=zip(a,b)
d=list(ak)
print(d)


for i in a:
    for j in b:
           c[j]=i
           b.remove(j)
           break
print(c)


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
# lis=[10,12,32,43,10,32,26,24,12]
#
# print(list(set(lis)))



