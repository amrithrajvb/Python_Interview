#function call itself(run repeatly)

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
    #n3 1+1=2
    #n4=2 + 1=3
nterms=10
print("fibanocci series")
for i in range(nterms):
    print(recur_fibo(i))

#loopexpllain

#first consider 0-9
#consider i=1 then go to function recur_fib(1) then condition check if condition check is ok return that data
#if consider 4th loop
# checking else condition 4-1)then go to function apply 3 we got that value of 3 from previous loop is 2
#then 4-2 is 2 loop 2 result is 1 then 1+2=3
