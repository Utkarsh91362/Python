class Employee:
    
    language="Py" #this is a class attribute
    salary="200000"

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("Creating an object")
    def getInfo(self):
        print(f'''The name of Employee is {self.name}.
The language is {self.language} and the salary is {self.salary}''')



Utkarsh= Employee("Utkarsh Kaushik",300000,"C++")
Utkarsh.getInfo()
