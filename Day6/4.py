class Employee:
    def setEmployee(self, empid, empname):
        self.empid = empid
        self.empname = empname

    def getEmployee(self):
        print(f"Employee ID: {self.empid} \nEmployee Name: {self.empname}")

class Payroll(Employee):
    def setPayroll(self, bs, hra, da):
        self.bs = bs
        self.hra = hra
        self.da = da

    def getPayroll(self):
        print(f"Base Salary: {self.bs} \nHRA: {self.hra} \nDA: {self.da}")

class Loan:
    def setLoan(self, amt):
        self.amt = amt

class Payslip(Payroll, Loan):
    def netSalary(self):
        gross_salary = self.bs + self.hra + self.da
        salary_on_hand = gross_salary - self.amt
        print(f"Gross Salary: {gross_salary}")
        print(f"Loan Deduction: {self.amt}")
        print(f"Salary on Hand: {salary_on_hand}")
        return salary_on_hand

Emp = Payslip()
Emp.setEmployee(1, "Rohan")
Emp.setPayroll(100000, 500, 200)
Emp.setLoan(1000)

Emp.getEmployee()
Emp.getPayroll()
Emp.netSalary()
