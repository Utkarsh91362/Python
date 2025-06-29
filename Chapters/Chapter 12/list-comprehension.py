myList=[1,2,4,9,21]

'''squaredList=[]
for i in myList:
    squaredList.append(i**2)

print(squaredList)'''

print("Using list comprehensions")

squaredList=[i**2 for i in myList]
print(squaredList)



l1=[1,7,2,11,22]
l2=[i for i in l1 if i>8 ]
print(f"l2 {l2}")
l1=[1,7,2,11,22]
l2=[item for item in l1 if item>8 ]
print(f"l2 {l2}")