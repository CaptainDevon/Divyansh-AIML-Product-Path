class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print("{}i+{}j".format(self.real,self.img))

num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()