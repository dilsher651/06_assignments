class Dog:
    def __init__(self, name, breed):
        self.name = name    # Instance variable
        self.breed = breed  # Instance variable
    
    def bark(self):         # Instance method
        print(f"{self.name} the {self.breed} says: Woof!")

# Create a Dog object
my_dog = Dog("Buddy", "Golden Retriever")

# Call the bark method
my_dog.bark()