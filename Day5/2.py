class Employee:
    def setEmployee(self,empid,empname,salary):
        self.empid = empid
        self.empname = empname
        self.salary = salary
    def display(self):
        print(f"Empid:- {self.empid}\nEmpname:- {self.empname}\nSalary:- {self.salary}")


emp = Employee()
emp.setEmployee(100,'Rohan',4343434)
emp.display()
