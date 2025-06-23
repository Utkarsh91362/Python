number=int(input("which multiplication table do you want? "))

#using for loop
print("using For loop")
for i in range(1,11):
    mul=number*i
    print(f"{number} X {i} = {mul}")

#using for loop in reverse
print("using for loop in reverse order")
for i in range(10,0,-1):
    mul=number*i
    print(f"{number} X {i} = {mul}")


    


#using while loop
print("using While loop")
i=1
while(i<11):
    mul=number*i
    print(f"{number} X {i} ={mul}")
    i+=1