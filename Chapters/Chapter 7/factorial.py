n=int(input("ENter the number: "))
fact1=1
for i in range(n,0,-1):
    fact1*=i
print(f"factorial is {fact1}")


#or
fact2=1
for i in range(1,n+1):
    fact2*=i
print(f"factorial is {fact2}")
