#even
range1= int(input("enter the minimum range"))
range2= int(input("enter the max range"))
for i in range(range1,range2):
    while i % 2 ==0:
        print(i)
        i += 1

 #odd
range1= int(input("enter the minimum range"))
range2= int(input("enter the maximum range"))
for i in range(range1,range2):
    while i % 2 !=0:
        print(i)
        i += 1

# if loop

range1= int(input("enter the minimum range"))
range2= int(input("enter the maximum range"))
for i in range(range1,range2):
    if i % 2 ==0:
        print(i)