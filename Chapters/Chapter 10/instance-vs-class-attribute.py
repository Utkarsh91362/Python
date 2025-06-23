class trial:
    
    a= 20 #class attribute

outside=trial()
print(trial.a,outside.a)

outside.a=0 # object attribute
print(trial.a,outside.a)

#instance attribute take preferance over class attributes during assignments and retrieval