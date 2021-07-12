inp=int(input("enter the limit"))
num=1
for i in range(0,inp):
    for j in range(0, i + 1):
        print(num,end=" ")
        num=num+1
    print()

def pattern(row):
    num=1
    for i in range(0, inp):
        for j in range(0, i + 1):
            print(num, end=" ")
            num = num + 1
        print("\r")
pattern(5)