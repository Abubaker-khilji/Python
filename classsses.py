class person:
    name = "abubaker"
    occupation = "data operator"
    company = "BTS Services Pvt (Ltd)"
    salary = "28000"
    def info(self):
        print(f"The Person is {self.name} and he/her is working as a {self.occupation} in {self.company} with monthly pay of {self.salary}")


a = person()
b= person()
b.name = "panda"
b.occupation = "graphic designer"
b.company = "null"
b.salary = "family money"

a.info()
b.info()

        

