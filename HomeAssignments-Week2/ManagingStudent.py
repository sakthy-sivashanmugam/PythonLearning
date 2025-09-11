class Student:
    def __init__(self, name, grade, department):
        self.name = name
        self.grade = grade
        self.department = department

    def print_info(self):
        return f"Name: {self.name}, Grade: {self.grade}, Department: {self.department}"
    
    def update_grade(self, new_grade):
        self.grade = new_grade

student1 = Student("Sakthy", "A", "Computer Science")
student2 = Student("Babu", "B", "Mathematics")
student3 = Student("Charles", "C", "Physics")

students = [student1, student2, student3]
for student in students:
    print(student.print_info())

print("\nAfter updating grade:\n")
student1.update_grade("A+")
for student in students:
    print(student.print_info())
