class Employee:
    a=1
    @classmethod  # the it will not show object attribute but will take class attribute
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


e=Employee()

e.name="Utkarsh Kaushik"
print(e.lname)
e.show()