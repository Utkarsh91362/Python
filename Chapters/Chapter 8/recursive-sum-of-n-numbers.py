#f(n)= n+ f(n-1)

def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)

x=int(input("Enter the nth natural number: "))
total=sum(x)
print(f"Sum of n natural numbers is {total}")