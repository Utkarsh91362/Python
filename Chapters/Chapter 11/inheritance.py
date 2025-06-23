class Employee: #parent class/ derived class
    company="ITC"
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")
    
'''class programmer:
    company="ITC Infotech"
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")
    def showLanguage(self):
        print(f"He is good with {self.language} language")'''


#reduced so much lines using inherited class 
class programmer(Employee):   #child class/ base class
    company="ITC Infotech"
    def showLanguage(self):
        print(f"He is good with {self.language} language")







a=Employee("Raghu", 23000, "C++")
b=programmer("Ravi", 30000, "Java")
print(a.company,b.company)