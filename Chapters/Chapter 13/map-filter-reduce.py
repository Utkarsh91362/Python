from functools import reduce

#map exmaple

l1=[1,2,3,4,5]

square= lambda x:x*x

sqList=map(square,l1)
for i in list(sqList):
    print(i)
sqList=map(square,l1)
print(list(sqList))


#filter example

def even(n):
    if (n%2==0):
        return True
    return False

onlyEven= filter(even,l1)
print(list(onlyEven))



#reduce example
def sum(a,b):
    return a+b

mul= lambda x,y: x*y
print(reduce(mul,l1))  # using sequential computation