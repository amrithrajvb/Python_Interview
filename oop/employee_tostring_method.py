class Employee:
    def printvalue(self,employeeName,experience):
        self.employeeName = employeeName
        self.experience=experience


    def print(self):
        print("Name:", self.employeeName)
        print("Esxperience", self.experience)

    def __str__(self):
        return self.employeeName+"experience is"+str(self.experience)

Emp=Employee()
Emp.printvalue("suresh",2)
Emp.print()
print(Emp)