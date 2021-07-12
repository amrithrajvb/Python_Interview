lis=[1,6,9,3,5,2]
#sor=[]
# lis.sort()
# print(lis)

for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i] > lis[j]:
            lis[i],lis[j]=lis[j],lis[i]
print(lis)
#print(sor)


#second method:
my_list=[111,-15,-26,15,1,0,8,876,54,23,-64,23,76]
new_list=[]
while my_list:
    min=my_list[0]
    for i in my_list:
        if i < min:
            min=i
    new_list.append(min)
    my_list.remove(min)
print(new_list)