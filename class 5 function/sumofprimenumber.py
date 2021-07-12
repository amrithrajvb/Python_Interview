no1= int(input("enter the minimum range"))
no2= int(input("enter the maximum range"))

sum=0
# if no1 & no2 > 1 :
for a in range(no1, no2):#collectig all values
    if a > 1:
      for i in range(2, a): # for checking prime numbers
          if (a % i) == 0:
              break
      else:
          #print(a)-for printing all prime numbers between range
          sum = sum + a
print(sum) #if we put under sum_sum + a looping...we just puting out side of the loop
