s1= {1,2,5,8}
s2= {2,8,3,7}
s3={2,8}

#all elements without repeat
print(s1.union(s2))

#only common elements
print(s1.intersection(s2))

#difference returns only the elements in first but not in the second.
print(s1-s2)


#symmetric difference returns element in either set but not in both i.e does not show common elements
print(s1^s2)



#check if no elements is common
print(s1.isdisjoint(s2))

# check if one set is subset of another
print(s3.issubset(s1))

#check if one is superset of another
print(s2.issuperset(s3))