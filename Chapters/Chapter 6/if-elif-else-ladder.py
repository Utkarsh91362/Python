a= int(input("Enter your age: "))

if(18<=a<80):
    print("Your are permitted to drive!")
elif(a>=80):
    print("You are too old to drive!")
elif(a<0):
    print("Age cannot be negative!")
elif(a==0):
    print("Age cannot be 0")
else:
    print("Your are too young to drive")
