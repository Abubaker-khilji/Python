class employee:
    def __init__(self,name,company):
        self.name = "dataguy"
        self.company = "xbox"
    company = "xbox"
    def show(self,name):
        print(f"the name is {self.name}and company is {self.company}")


    @classmethod
    def changecompnay(cls,newcopany):#argument as a instance milta hai
            cls.company = newcopany

e1 = employee("dataguy","xbox")
e1.name = "dataguy"
e1.show( "dataguy")
e1.changecompnay("sony")
e1.show( "dataguy")
print(employee.company)            