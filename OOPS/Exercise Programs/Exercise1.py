class Vehicle:
    name=""
    kind="car"
    color=""
    value=100.00

    def __init__(self,name,color):
            self.name=name
            self.color=color
        
    def description(self):
        descStr="%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        print(descStr)
    

car1=Vehicle("Manza","Marcho Red")
car2=Vehicle("Carens","Maroon")
car3=Vehicle("WagonR","Brown")

car1.description()
car2.description()
car3.description()