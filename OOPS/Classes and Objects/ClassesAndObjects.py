class Sample:
    variable="blah"

    def memberFunction(self):
        print("This is the message from the class and has "+self.variable)


s=Sample()
s.memberFunction()
print(s.variable) 
