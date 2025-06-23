with open("txt files/poem.md") as f:
    data=f.read()
    if("twinkle" in data):
        print("The word 'Twinkle' is present in the content")
    else:
        print("The word 'Twinkle is not present in the content")
        