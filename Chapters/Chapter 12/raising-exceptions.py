a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))

if(b==0):
    raise ZeroDivisionError("infinite")
else:
    print(f"The division {a/b} is {a/b}")