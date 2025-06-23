
def greatest(a,b,c):
    if(a==b and b==c):
        print("The numbers are equal!")
    elif(a>=b and a>=c):
        print(f"{a} is the greatest")
    elif(b>=a and b>=c):
        print(f"{b} is the greatest")
    elif(c>=b and c>=a):
        print(f"{c} is the greatest")
    else:
        print("Enter a valid number")

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
z = int(input("Enter number 3: "))
greatest(x,y,z)




