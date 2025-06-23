s= {5,1,4,734,234,62,12}

#add element
s.add(3)
print(s)

#remove element
s.remove(4)
print(s)  # will give an error if the element does not exist in the set

#discard element
s.discard(4)
print(s) # will remove element and would not given an error is the element doesn't already exist in the set


#remove random element
d={ "hi","I","am","Utkarsh"}
print(d)
d.pop()
print(d) #mostly the first element after a sort of aranging them in order


#clear removes all elements
d.clear()
print(d)
