class Employee:
    def __init__(self ,  name , id):
        self.name = name
        self.id = id
        

    def showdetails(self):
        print(f'the name of emplyee is {self.name} and id {self.id}')


class programmer(Employee):
    def showlanguage(self):
        print("the default language is python")

#simple bat yeh hai k inheritnace tub chulti jub hum apnay inhheit jis mein kurwaya gya hai woh chulaye tub chulti hai mtlb beta chlay ga baap nhi hahahahahah  

class seniordeveloper(programmer):
    def __init__(self, projects="Unknown", company="Unknown"):
        self.projects = projects
        self.company = company
        
    def expertise(self):
        self.company = input("Enter the name of the company engineer has worked at: ")
        self.projects = input("Please enter the projects the engineer has worked on: ")
        print(f"He is a senior software engineer who has worked at {self.company}.")
        print(f"The engineer has worked on the following projects: {self.projects}")
         

e1 = Employee("rehman aslam", 400)
e1.showdetails()
e2 = programmer("khilji", 4400022)
e2.showdetails()
e2.showlanguage()
e3 = seniordeveloper()
e3.expertise()

