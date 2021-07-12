#unexpected errors, when provide error in input

#exception handling....solve unexcepcted error

#try...exceptional code (try block execute everytime)
#except...solving code
#finally....anything

n=int(input("number"))
n2=int(input("number2"))
try:
    print(n/n2)
except Exception as e:#exception module as-keyword  e-variable
    print("exception occured",e)
finally:
    print("inside finally")