class Student:
    def __init__(self, name, student_id, grades=[]):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def display_info(self):
        print(f"Student: {self.name}, ID: {self.student_id}, Average Grade: {self.get_average():.2f}")

# Example Usage
if __name__ == "__main__":
    student1 = Student("John", "S123", [85, 90])
    student1.add_grade(95)
    student1.display_info()
