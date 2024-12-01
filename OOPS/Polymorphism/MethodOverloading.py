class User:
    def printInfo(self,name,age=None):
        if age==None:
            self.name=name
            print("Hello {}".format(self.name))
        else:
            self.name=name
            self.age=age
            print("Hello {} your age is {}".format(self.name,self.age))


u=User()
u.printInfo("Divyansh")
u.printInfo("sumit",50)