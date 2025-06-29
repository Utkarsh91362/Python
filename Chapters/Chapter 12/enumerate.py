l=[3,512,42,533]
'''index=0
for i in l:
    print(f"The item number {index} is {i}")
    index+=1'''


#or
print("Using enumerate func")

for index,i in enumerate(l):
    print(f"The item number {index} is {i}")