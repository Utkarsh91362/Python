n=int(input("Enter the number: "))

'''for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break
else:
    print("it is a prime number")
'''

#using while loop
i=2
while(i<n):
    if(n%i)==0:
        print("number is not prime")
        break
    i+=1
else:
    print("it is a prime number")