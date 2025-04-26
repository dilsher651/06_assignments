class Person:
    def __init__(self, name):
        self.name = name  # Initialize base class attribute

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent class constructor
        self.subject = subject  # Add subclass-specific attribute

    def display(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

# Create a Teacher object
teacher = Teacher("Dr. Smith", "Computer Science")
teacher.display()