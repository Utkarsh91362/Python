def pattern1(n):
    if(n==1):
        print( "*")
    else:
        print("*"*n)
        pattern1(n-1)
print("from top to bottom")    
pattern1(4)

print("\nfrom bottom to top")
def pattern2(n):
    if n == 1:
        print("*")
    else:
        pattern2(n - 1)
        print("*" * n)

pattern2(4)