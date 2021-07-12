s={0,1,2,3,4,5,6,88,65,98,34,11,19}
odd=set()
even=set()
for i in s:
    if i % 2 == 0:
        even.add(i)
    else:
        odd.add(i)
print("odd numbers are",odd)#sorted(odd)-will sort but it convert to lIST
print("even numbers are",even)
