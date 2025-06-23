class Employee:
    a=1
    @classmethod  # the it will not show object attribute but will take class attribute
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

e=Employee()
e.a=45
e.show()