class Employee:
    def __init__(self):
        print("constructor of emplopyee")
    a=1
class programmer(Employee):
    def __init__(self):
        
        print("constructor of programmer")
    b=2
class manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c=3
o=manager()
print(o.a)