def divisible5(n):
    if(n%5==0):
        return True
    return False

a=[42, 87, 19, 65, 3, 78, 50,55, 11, 94, 27]

f=list(filter(divisible5,a))
print(f)