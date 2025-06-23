import re
word="Donkey"
with open("txt files/donkey.txt", "r") as f:
    content = f.read()

content= re.sub("Donkey","###",content, flags=re.IGNORECASE)
with open("txt files/donkey.txt","w") as f:
    f.write(content)
    print("work done")