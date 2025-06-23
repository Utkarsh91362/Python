a=(1,45,343,2345, False, "Rohan", "shivam")
print(a)

#count
no= a.count(45)
print(no)

#index finding
i=a.index(False)
print(i)


#repeated tuple
repeated= a*4
print(repeated)


#To check if the element exists in the tuple or not
print(234 in a)
print(2345 in a)

# length of tuple
print(len(repeated))


#slicing
sliced = a[2:6]
print(sliced)
print(a)

#unpacking tuple elements with individual variables
b= (1,2,3,4)
x , y,z= b  # no. of vaariables should eb exactly the length of the tuple
print(x,y,z)