def rectangle(n):
    for i in range(0,n):
        print(" "*i,end=" ")
        for j in range(0,n):
         print("*",end=" ")
        print()
rectangle(4)

#parrellelstructure

def rectangle(n):
    for i in range(0,n):
        print(" "*i,end=" ")
        for j in range(0,n):
         print("*",end=" ")
        print()
rectangle(4)


#parellel opposite
def rectangle(n):
    for i in range(0,n):
        print(" "*(n-i),end=" ")
        for j in range(0,n):
         print("*",end=" ")
        print()
rectangle(4)


def paralell(n):
    k=n
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k= k-1
        for j in range(0,n):
            print("*", end=" ")
        print()
rectangle(4)