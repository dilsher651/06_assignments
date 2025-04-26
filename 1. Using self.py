class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage:
student1 = Student("Dilber", 95)
student1.display()

student2 = Student("ayaan", 98)
student2.display()
