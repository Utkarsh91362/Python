class calculator:
    def __init__(self,number):
        self.number=number
    
    @staticmethod
    def greet():
        print("Hello User!!")
    
    def square(self):
        print(f"Square of {self.number} is {self.number ** 2}")
    
    def cube(self):
        print(f"Cube of {self.number} is {self.number ** 3}")
    
    def sqrt(self):
        print(f"Square root of {self.number} is {self.number ** 0.5}")

calculator.greet()
n=int(input("Enter the number :"))
number= calculator(n)

number.square()
number.cube()
number.sqrt()