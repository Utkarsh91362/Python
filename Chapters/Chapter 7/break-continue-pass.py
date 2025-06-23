#break
for i in range(50):
    if(i==37):
        break
    print(i)
else:
    print("done")  # this will not execute because break is present in for loop

#continue
for i in range(30):
    if(i==12 or i==22 ):
        continue #will skip this iteration
    print(i)
else:
    print("done") #will execute beacuse the whole loop was executed completely



#pass
for i in range(34):
    pass

i=0
while(i<12):
    print(i)
    i+=1
