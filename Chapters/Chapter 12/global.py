a=89  #a is global variable 
def func():
    global a
    a=3    #a is local variable for this func
    print(a)

func()
print(a)