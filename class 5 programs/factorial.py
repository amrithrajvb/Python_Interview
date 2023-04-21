# inp=int(input("enter the number"))
# if inp > 0:
#    fact = 1
#    for i in range(1, inp + 1):
#       fact = fact * i
#    print(fact)
# elif inp == 0:
#    print("factorial of 0 is 1")
# else:
#    print("print positive number")
str = "abcbababc"
test = "abc"
count = 0
for i in range(len(str)-1):
   if str[i] == test[0]:
      if str[i + 1] == test[1]:
         if str[i + 2] == test[2]:
            count = count + 1
            # i = i + 3

print(count)


