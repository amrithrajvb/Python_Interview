#
def pattern(row):
    for i in range(row, 0 ,- 1):
        for j in range(0, i):
            print("*", end="")
        print()  # print("\r")

pattern(4)

inp=int(input("enter the limit"))
for i in range(inp, 0, - 1):#for for i in range(inp,0)
    for j in range(0, i):#for j n range(0,n-i)
        print("*", end="")
    print()  # print("\r")

