s={0,1,2,3,4,5,6,88,65,98,34,11,19,22}
S1={1,2,3,4,19,10}
set1=set()
for i in s:
    if i in S1:
        set1.add(i)
        print(i)
print(set1)