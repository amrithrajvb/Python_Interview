inp=int(input("enter the number"))
if inp > 0:
   fact = 1
   for i in range(1, inp + 1):
      fact = fact * i
   print(fact)
elif inp == 0:
   print("factorial of 0 is 1")
else:
   print("print positive number")