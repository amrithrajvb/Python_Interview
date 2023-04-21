# b=[i for i in range(20) if i % 2 == 0]
# print(b)

c=[i for i in range(5) if i % 4==0]
print(c)
d=list(filter(lambda num:num%4==0,c))
print(d)
#
# #find all the numbers from 1 to 1000 that are divisible by 8
#
# c=[i for i in range(1,1000) if i % 8 == 0]
# print(c)
# print(len(c))