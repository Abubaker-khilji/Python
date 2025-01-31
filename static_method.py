class math:
    def __init__(self, num):
          self.num = num



    def addtonum(self,n):
         self.n = self.num +n

    @staticmethod #we dont need to use self instance in staticmethod decorator 
    def add(a,b):
       return a+b



a = math(5)
print(a.num)                   
a.addtonum(6)
print(a.num)


print (math.add(5554545552585,45454854845))