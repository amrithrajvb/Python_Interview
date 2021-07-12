s={1,2,3,4,5,6,7,8,9,0,17}
prime=set()
nonprime=set()
for i in s:
    if i > 1:
        for j in range(2,i):# for j in range(2,2) no loop is availabale then go to else condiTION
            if (i % j) == 0:
                nonprime.add(i)
                break
        else:
            prime.add(i)
print("prime",prime)
print("non prime",nonprime)