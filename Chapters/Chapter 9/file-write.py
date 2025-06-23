st= "Hey, this will be the next line added by file-write.py ."
f=open("txt files/file.md", "w")  #this will overwrite the file if you want to append(add) then use "a" 
f.write("Hi\n")          #f.write() can be used multiple times
f.write("hello\n")
f.write("bye")
f.close()
f=open("txt files/file.md", "r")  #opening the file again to read
data=f.read()
print(data)