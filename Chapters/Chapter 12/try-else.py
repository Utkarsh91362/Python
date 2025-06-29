try:
    a=int(input("Enter number 1:"))
    print(a)

except Exception as e:
    print(e)

else:                       #This only runs if the try was successful
    print("I am inside else")