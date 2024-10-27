class Student:
    def __init__(self,rollno,name,fee):
        self.rollno = rollno
        self.name = name
        self.fee = fee

    def display(self):
        print(f"Rollno:- {self.rollno} \nName:- {self.name} \nFee:- {self.fee}")

student = Student(1,"rohan",5000)
student.display()
