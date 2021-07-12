class Employee:
    def printvalue(self,employeeName,experience):
        self.employeeName = employeeName
        self.experience=experience


    def print(self):
        print("Name:", self.employeeName)
        print("Experience", self.experience)

    def __str__(self):
        return self.employeeName+"experience is"+str(self.experience)

Emp=Employee()
Emp.printvalue("amrith",2)
Emp.print()
print(Emp)