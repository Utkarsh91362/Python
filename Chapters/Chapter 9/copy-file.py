
with open("txt files/file.md") as f:
    content=f.read()
with open("txt files/copy1.md","w") as f:
    f.write(content)
