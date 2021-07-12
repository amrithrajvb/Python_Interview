# lst=[1,2,3,4,5,6]
#
# #map used for we consider to display all elements related output #map(function,iterable)
# #filter mainly used for filter the element and there should be one condition #filter(function,iterable)
#
# square=list(map(lambda num:num**2,lst))
# print(square)
#
# #to print all the even numbers
#
# even=list(filter(lambda num:num%2==0,lst))
# print(even)

#print if num<5 num-1 else num+1

lsst=[2,3,4,8,10,7]
lsst=[1,2,3,4,5,6,7]#second
# ls=[]
# for i in lsst:
#     if i<5:
#        ls.append(i-1)
#     else:
#         ls.append(i+1)
#
#
# print(ls)

#x-1 if x < 5 else x+1-territorry method
numbe=list(map(lambda x:x-1 if x < 5 else x+1,lsst))
print(numbe)

#use of more than one if condition

result=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lsst))
print(result)