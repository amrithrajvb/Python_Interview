inp=input("enter the string")
symbol='''@!`#$%^&*()_+<>,'".:{}[]?/\|"'''#using triple quotes with starting
#punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
c=""
for i in inp:
    if i not in symbol:
        c=c+i
print(c)