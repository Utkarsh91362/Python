class Programmer:
    Company= "Microsoft"
    def __init__(self, name, salary , pin):
        print("Microsoft Corporate")
        self.name=name
        self.salary=salary
        self.pin=pin
    def getDetails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Pincode: {self.pin}\n")

u= Programmer("Utkarsh",120000,201003)
a= Programmer("Arnim",140000,204013)
s= Programmer("Saksham",110000,248007)
r= Programmer("Rajat",100000,201013)


u.getDetails()
a.getDetails()
s.getDetails()
r.getDetails()