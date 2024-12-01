class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def getAvg(self):
        sum=0
        for i in range(0,len(self.marks)):
            sum+=self.marks[i]

        print("The average the student has scored is %f"%(sum/(len(self.marks))))

    @staticmethod
    def display():           #this doesnt have the self argument
        print("This students studies in Vignan Bo Tree School")
    


s1=Student("Divyansh",[96,95,94,86,84])
s1.getAvg()


s1.display()