# length
word="advanced-playground"

print(len(word))


# ends with
print(word.endswith("und"))

#startswith
print(word.startswith("Ad"))
print(word.startswith("ad"))    #capital and small are considered different

#capatilize it will capitilize the first letter
print(word.capitalize())    
print(word.title())  #advanced and playground are considered 2 different words 
print("Hello".swapcase())  # reverse the case




#splitting string to list
name="A,B,C"
print(name.split(","))
print("Amazing".split("z"))



#replace letter or words
a="Amazed"
print(a)
print(a.replace("ed","ing"))