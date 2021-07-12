def add(*args):
    print(args)#returns tuple value
    sum=0
    for i in args:
        sum+=i
    print(sum)
add(1,2,3,4)


#when we specify the datas in function call--using**args and result return as dictionary

def printvalue(**args):
    print(args)
printvalue(id=1,name="suresh",place="kochi",salary=10000)