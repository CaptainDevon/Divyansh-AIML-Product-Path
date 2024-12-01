class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"


s1=Student(99,98,89)
print(s1.percentage)

s1.phy=90
print(s1.phy)
print(s1.percentage)