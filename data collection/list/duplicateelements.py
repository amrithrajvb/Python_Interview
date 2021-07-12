lis=[10,12,32,43,10,32,26,24,12]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i] ==lis[j]:
            print(lis[i])

#second

b=[]
for i in lis:
    if i not in b:#take all the elements when the repeated value then else will work.
        b.append(i)
    else:
        print("hh",i)



