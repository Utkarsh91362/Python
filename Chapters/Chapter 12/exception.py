try:
    a=int(input("Enter a number: "))
    print(a)
except ValueError as v:
    print("Wrong Value")

except Exception as e:
    print(e)
    print("Thank You")