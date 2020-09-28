
class Employee:
    appraise = 1.04
    EMP_Count = 0
    def __init__(self,first,last,pay,age):
        self.first = first
        self.last = last
        self.pay = pay
        self.age = age
        Employee.EMP_Count += 1
    def display(self):
        print(self.last," works in Qburst")
    def apply_appraisal(self):
        self.pay = self.pay * 1.04
        print("New salary for",self.last, "is",self.pay)

emp1 = Employee("Mohammed","Eza",50000,22)
emp2 = Employee("Mohammed","Abshar",60000,23)
emp1.apply_appraisal()
emp2.apply_appraisal()
print("The number of employees is",Employee.EMP_Count)
print(emp1.__dict__)
print(Employee.__dict__)
#emp1.appraise = 1.05
#print(emp1.__dict__)


