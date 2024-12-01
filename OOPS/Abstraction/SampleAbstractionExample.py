class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started..")
        self.clutch=False

    def stop(self):
        self.brk=True
        self.acc=False
        print("The Car has Stopped..")
        self.brk=False


car1=Car()
car1.start()
car1.stop()
