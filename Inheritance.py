class person :
    upper=1
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class police (person):
    def __init__(self,fname,lname,salary):
        person.__init__(self,fname,lname)
        self.salary = salary
    def policeinfo (self):
        self.printname()
        print("Salary is ",self.salary,self.upper)

emp1 = person("Mohammed","Eza")
emp1.printname()
police1= police("Lewis","Caral",50000)
police1.policeinfo()
print(police.__dict__)