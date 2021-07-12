lis=[1,6,9,3,5,2]
#sor=[]
# lis.sort()
# print(lis)

for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i] > lis[j]:
            lis[i],lis[j]=lis[j],lis[i]
print("minimum",lis[0])
print("maximum",lis[-1])

#second method
#
# lis.sort()
# print("minimum",lis[0])
# print("maximum",lis[-1])