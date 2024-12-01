class NumberHolder:

    def __init__(self,number):
        self.number=number

    def returnNumber(self):
        return self.number
    

var=NumberHolder(10)
print(var.returnNumber())