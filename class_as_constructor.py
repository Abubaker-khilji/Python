class employee:
    def __init__(self , name , salary): # yeh constructor hai class ka 
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],
                   int(string.split("-")[1]))

e1 = employee("dabiyal",52021)
print(e1.name)
print(e1.salary)


string = "khilji-5555500"
e2 = employee.fromstr(string)
print(e2.name)