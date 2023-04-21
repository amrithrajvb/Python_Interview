#append - toappend the list but in the case of 2 list , getting nested list
#extend
lst=[1,2,5,6]
b=[8,9,7]
b.append(10)
print(b)
c=lst
print(c)
lst.extend(b)
print(lst)



def factorial(x):
    if x ==1:
        return 1

    else:
        return x*factorial(x-1)


print(factorial(5))
