class twoD_Vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class threeD_Vector(twoD_Vector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a=twoD_Vector(1,3)
b=threeD_Vector(2,4,8)
a.show()
b.show()