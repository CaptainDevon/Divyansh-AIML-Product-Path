class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price>ord2.price
    

Ord1=Order("Chips",20)
Ord2=Order("Cookie",40)

print(Ord1>Ord2)