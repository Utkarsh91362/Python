class Employee:
    
    language="Py" #this is a class attribute
    salary="200000"
Utkarsh= Employee()
Utkarsh.name="Utkarsh Kaushik" # this is an instance/object attribute
print(Utkarsh.name,Utkarsh.salary,Utkarsh.language)

rohan=Employee()
rohan.name="Rohan Rao"
print(rohan.name,rohan.salary,rohan.language)

# Here language and salary are class attributes but name is an instance/ obejct attribute