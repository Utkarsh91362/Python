class Employee: 
    company="ITC"
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language


    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder:   # coder is the child class of Employee inheriting all properties of Employee
    def printLanguages(self,language):
        self.language=language
        print(f"out of all the languages here is your language: {self.language}")


class programmer(Employee,Coder):   # programmer is the child class of Coder thus it inherits all property of Coder as well as Employee
    company="ITC Infotech"
    

b=programmer("Ravi", 30000, "Java")
b.printLanguages("Python")
print(b.name)