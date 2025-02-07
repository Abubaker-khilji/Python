class father:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def info(self):
        return f"Your father is {self.name}, works as a {self.work}, and his age is {self.age}."


class beta(father):
    def __init__(self, name, age, work, beta_name, beta_school, beta_age):
        # Call the __init__ method of the father class
        super().__init__(name, age, work)
        # Add specific attributes for beta
        self.beta_name = beta_name
        self.beta_school = beta_school
        self.beta_age = beta_age

    def info(self):
        # Call father class's info method and add beta-related details
        father_info = super().info()
        return f"{father_info} The beta's name is {self.beta_name}, he studies at {self.beta_school}, and he is {self.beta_age} years old."


# User input for father details
father_name = input("Enter your father's name: ")
father_age = input("Enter your father's age: ")
father_work = input("Enter your father's work: ")

# Create a father instance
father1 = father(father_name, father_age, father_work)
print(father1.info())

# User input for beta details
beta_name = input("Enter the beta's name: ")
beta_school = input("Enter the beta's school name: ")
beta_age = input("Enter the beta's age: ")

# Create a beta instance, using the same father details for this example
beta1 = beta(father_name, father_age, father_work, beta_name, beta_school, beta_age)
print(beta1.info())
