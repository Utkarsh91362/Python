class Number:
    def __init__(self,n):
        self.n=n
    
    def __add__(self,num):
        return self.n + num.n
    def __mul__(self,num):
        return self.n * num.n
    def __truediv__(self,num):
        return self.n / num.n
    def __len__(self):
        return len(str(self.n))

n=Number(55)
m=Number(4)

print(n/m)