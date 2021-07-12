lis=[2,4,5,69,34,32,12,11,17]
odd=[]
even=[]
for i in lis:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("odd",odd)
print("even",even)