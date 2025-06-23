import re
words=["Donkey","Bad","sacks","the"]
with open("txt files/donkey.md", "r") as f:
    content = f.read()
for word in words:
    content= re.sub(word,"#"*len(word),content, flags=re.IGNORECASE)
    with open("txt files/donkey.md","w") as f:
        f.write(content)
    print("work done")