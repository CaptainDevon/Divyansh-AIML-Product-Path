class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return (22/7) * self.radius * self.radius
    
    def perimeter(self):
        return 2* (22/7)* self.radius
    

c=Circle(7)
print(c.area())
print(c.perimeter())