class Employee:
    def setEmployee(self,empid,empname):
        self.empid = empid
        self.empname = empname

    def getEmployee(self):
        print(f"Employee ID:- {self.empid} \nEmployee name:- {self.empname}")

class Payroll(Employee):
    def setPayroll(self,bs,hra,da):
        self.bs = bs
        self.hra = hra
        self.da = da
    
    def getPayroll(self):
        print(f"Base salary:- {self.bs} \nhra:- {self.hra} \nda:- {self.da}")


class Payslip(Payroll):
    def netSalary(self):
        return self.bs + self.da + self.hra


Emp = Payslip()
Emp.setEmployee(1,"Rohan")
Emp.setPayroll(100000,500,200)
print(f"The total salary of {Emp.empname} is {Emp.netSalary()}")
