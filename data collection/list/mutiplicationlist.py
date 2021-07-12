lis=[2,4,65,4,7,8]
# mul=[]
# for i in lis:
#     b= i* 5
#     mul.append(b)#mut.append(i*5)
# print(mul)

##effective
b=[i*5 for i in lis]##list comprehension,first element should be which element to be add, space for each conditions
print(b)
