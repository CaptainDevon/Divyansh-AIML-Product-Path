class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role: {}".format(self.role))
        print("dept: {}".format(self.dept))
        print("salary: {}".format(self.salary))

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT",75000)


engg1=Engineer("Divyansh Sinha",20)
engg1.showDetails()