marks= { "a": 100, "b": [7,8,9], "c": 89}

print(marks, type(marks))

print(marks["b"])

#to print key value pair
print(marks.items())

#to print keys
print(marks.keys())

#to print values 
print(marks.values())

#to update
marks.update({"a": 99})  #if there is a key wtih that index then it will be updated otherwise a new key value pair will be created
print(marks)


#fetch values
print(marks.get("Harry")) #prints None
#print(marks("Harry"))    #prints error
#both looks same but the get statement will return "None" if the key doesn't exist but this statement will result in error



#delete a key value pair through the key
marks.pop("b")
print(marks)

marks.update({"d":32})

#to delete last added item to the dictionary
marks.popitem()
print(marks)


#making a copy
m2= marks.copy()
print(m2)


marks.setdefault("country", "india")
print(len(marks))