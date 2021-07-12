a=[1,2,3,4]
b=int(input("enter the element to be search"))
try:
    print(a[b])#index error
except Exception as e:
    print("exception is",e)
finally:
    print("result")


