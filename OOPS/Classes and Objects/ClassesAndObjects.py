class SampleClass:
    variable="blah"

    def memberFunction(self):
        print("This is the message from the class and has "+self.variable)


s=SampleClass()
s.memberFunction()
print(s.variable) 
