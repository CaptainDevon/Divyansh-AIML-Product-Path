class Account:
    def __init__(self,*args):
        if(len(args)==2):
            self.accName=args[0]
            self.balance=args[1]

            print("Welcome {} your amount is added".format(self.accName))

        elif len(args)==1:
            self.accName=args[0]
            self.balance=0

            print("Welcome {}".format(self.accName))

        

    def credit(self,amount):
        if self.balance==0:
            print("Insufficient Balance")

        else:
            self.balance-=amount
            print("{} rupees is credited from your bank account".format(amount))

    def debit(self,amount):
        self.balance=amount
        print("{} rupees is debited to your account".format(amount))

    def printBalance(self):
        print("{} = {} rupees".format(self.accName,self.balance))


user1=Account("Sumit")
user2=Account("Divyansh",100000)
user1.printBalance()
user2.printBalance()
user1.credit(500)
user1.debit(1000)
user1.credit(200)
user1.printBalance()

user2.credit(8000)
user2.debit(5000)
user2.printBalance()




