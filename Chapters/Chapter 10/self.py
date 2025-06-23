class Employee:
    
    language="Py" #this is a class attribute
    salary="200000"

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
    
    def greet(self):
        print(f"Hello!, {self.name}")



Utkarsh= Employee()
Utkarsh.name="Utkarsh Kaushik" # this is an instance/object attribute
Utkarsh.language="Java"
Utkarsh.getInfo()
Utkarsh.greet()