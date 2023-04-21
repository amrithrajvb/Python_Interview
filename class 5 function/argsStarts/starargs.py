def add(*args):
    for i in range(len(args)):
        for j in range(i+1,len(args)):
            if args[i]+args[j]==4:
                print(args[i],args[j])


    # print(args)#returns tuple value
    # sum=0
    # for i in args:
    #     sum+=i
    # print(sum)
add(1,2,3,4,2)





#when we specify the datas in function call--using**args and result return as dictionary

def printvalue(**args):
    print(args)
    for key,value in args.items():
        print("{} is {}".format(key, value))


printvalue(id=1,name="suresh",place="kochi",salary=10000)