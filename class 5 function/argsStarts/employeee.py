employee={
    1000:{"eid":1000,"ename":"ajay","salary":34000,"designation":"developer"},
    1001:{"eid":1001,"ename":"arun","salary":38000,"designation":"developer"},
    1002:{"eid":1002,"ename":"akhil","salary":210000,"designation":"hr"},
    1003:{"eid":1002,"ename":"anu","salary":45000,"designation":"analyst"}
}

#print name of employee whose eid=1002

print(employee[1002]['ename'])
#full print print(employee[1002])


print(employee[1000]["designation"])
inp=1009
abc="salary"

if inp in employee and abc in employee[inp]:
    print(employee[inp])
else:
    print("sorry")