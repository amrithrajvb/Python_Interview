#if we want to populate only get one value then use reduce like highest,lowest,total

#print,input,type included into bultins.py module

#reduce included functools
#we can only return integer value

from functools import reduce
lis=[1,2,3,4,5,6,7]
total=reduce(lambda num1,num2:num1+num2,lis)
print(total)

#highest-return only one value

high=reduce(lambda num1,num2:num1 if num1>num2 else num2,lis)
print(high)
