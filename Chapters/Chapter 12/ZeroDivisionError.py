try:
    a=int(input("Enter number 1:"))
    b=int(input("Enter number 2:"))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")