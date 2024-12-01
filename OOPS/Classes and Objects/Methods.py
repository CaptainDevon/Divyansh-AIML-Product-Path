class Arithematic:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    #Methods
    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def mul(self):
        return self.a*self.b
    
a=Arithematic(5,4)
print(a.add())
print(a.sub())
print(a.mul())