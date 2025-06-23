'''
for n=3
  *
 ***
*****'''

n= int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1))



print("\nPattern 2")
'''
for n=3
*
**
***
'''

for i in range(1,n+1):
    print("*"*(i))



print("\nPattern 3")
'''
* * *
*   *
* * * 
for n=3
'''
for i in range(1,n+1):
    if(i==1 or i==n):
        print("* "*n)
    else:
        print("* ",end="")
        print("  "*(n-2),end="")
        print("* ")
print("")

