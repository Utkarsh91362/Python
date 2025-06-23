f=open("txt files/file.md")
#lines= f.readlines()
#print(lines,type(lines)) #type(lines) tell us the lines are being stored in a list

line1= f.readline()
print(line1,type(line1)) 
line2= f.readline()
print(line2,type(line2)) 
line3= f.readline()
print(line3,type(line3)) 
line4= f.readline()
print(line4,type(line4)) 
line5= f.readline() #returns false if the line is not empty
print(line5=="") 
f.close()



print("\nMethod 2\n")

f=open("txt files/file.md")
line=f.readline()
while(line !=""):
    print(line)
    line=f.readline()
f.close()