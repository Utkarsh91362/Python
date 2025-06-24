class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,second):
        result=vector(self.x+second.x,self.y+second.y,self.z+second.z)
        return result
    def __mul__(self,second):
        result=self.x * second.x + self.y * second.y + self.z * second.z 
        return result
    
    def __str__(self):
        return f"Resultant Vector is ({self.x}i +{self.y}j +{self.z}k)"
    def __len__(self):
        return 
        


v1=vector(2,3,4)
v2=vector(3,10,8)


print(f"Dot Product: {v1.__mul__(v2)}\nAddition :{v1.__add__(v2)}")