#class help us create group of functions of same uses
#two types var class and instance types 

class employee:
    company = "xbox"
    no_of_employee = 0
    def __init__(self,name,position):
         self.name = name
         self.position = position
         self.raise_pay = 0.55
         employee.no_of_employee +=1

    def showempdetail(self):
         input 
         print(f"the name of employee is {self.name} and salary is {self.raise_pay} and he/her work as on {self.position} in {self.company}")     
          

emp1 = employee("harry","pythoncoder")
emp1.raise_pay = 0.3
emp1.company = "sony"
emp1.showempdetail()