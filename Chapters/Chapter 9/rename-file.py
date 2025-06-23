o=input("enter the old file name:")
n=input("what do you want to replace it with: ")
with open(f"txt files/{o}")as f:
    content=f.read()
with open(f"txt files/{n}","w")as f:
    f.write(content)

import os
os.remove(f"txt files/{o}")
print("file name replaced")
