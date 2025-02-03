class employee:
    company = "xbox"
    def show(self):
        print(f"the name is {self.name}and company is {self.company}")


    @classmethod
    def changecompnay(cls,newcopany):#argument as a instance milta hai
            cls.company = newcopany

e1 = employee()
e1.name = "dataguy"
e1.show()
e1.changecompnay("sony")
e1.show()
print(employee.company)            