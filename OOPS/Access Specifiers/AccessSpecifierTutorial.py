class Account:
    def __init__(self,accNO,accPass):
        self.__acc_no=accNO
        self.__acc_pass=accPass

    def getID(self):
        return self.__acc_no


acc1=Account("12345","abcde")
print(acc1.getID())



# __ before any variable or method name
