#bracket () is not nessasary for creating tuple but we should keep bracket in empty tuple
#immutable
#heterogenous
#index possible


tup=(1,2,3,4,5,67,3)#tup=1,2,3,4,56,7
print(tup)
print(type(tup))
tup=()
print(tup)
print(type(tup))


#keywords(max,min,len)
tup2=(1,2,3,4,5,67,3)
print("max",max(tup2))
print("min",min(tup2))
print("length",len(tup2))

tup2=1,2,'hai'
print(tup2)
print(tup2[1])
print(tup2[-1])

