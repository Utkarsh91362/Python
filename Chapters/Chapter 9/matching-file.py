with open("txt files/file.md")as f:
    content1= f.read()
with open("txt files/copy1.md")as f:
    content2= f.read()

if(content1==content2):
    print("Identical files")
else:
    print("separate files")
