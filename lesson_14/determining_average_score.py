class Student():
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def update_average_score(self, new_score): # method for changing the GPA
        self.average_score = new_score

    def display_info(self):
        print(f"Student: {self.name} {self.surname}, Age: {self.age}, Average score: {self.average_score}")

# Creation of the student object
student_1 = Student("Olya", "Yuthevich", 20, 4.8)

student_1.display_info()

student_1.update_average_score(5.0)

print(f"Updated GPA data:")

student_1.display_info()
