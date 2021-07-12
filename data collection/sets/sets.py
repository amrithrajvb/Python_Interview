#sets-to store elements
#doesn't store duplicate elements
#order doesn't keep
#mutable (we can update all time)

set1={1,4,5,99,2,55,90,7,4,1,2,3,2,1}
print(set1)
print(type(set1))

#set2={}## it should be dict as type
#hetrogeneous collection of data(occupy diffirent type of data)
set2=set()## type is set
print(type(set2))
set2.add("hello")
set2.add(6)
set2.add(9.8)
set2.add(True)
print(set2)

#set iteration
s={1,2,3,4,5,6,7,8,9,0}
for i in s:
    print(i)

#nesting-nesting is not possible in set
set1={1,2,{3}}