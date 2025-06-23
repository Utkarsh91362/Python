def avg():       #function definition
    a=int(input("Enter Number 1:"))
    b=int(input("Enter Number 2:"))
    c=int(input("Enter Number 3:"))
    average=(a+b+c)/3
    return average

print(f"the average is {avg():.2f}")   #avg() is called function call