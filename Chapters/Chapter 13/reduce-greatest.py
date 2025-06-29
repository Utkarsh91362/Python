from functools import reduce
l=[42, 87, 19, 65, 3, 78, 50,55, 11, 94, 27]

def greater(a,b):
    if(a>b):
        return a
    else:
        return b
    
f=reduce(greater,l)
print(f)