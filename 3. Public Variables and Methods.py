class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):       # Public method
        print(f"{self.brand} car started! Vroom vroom!")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Brand:", my_car.brand)  # Output: Brand: Toyota

# Call public method
my_car.start()  # Output: Toyota car started! Vroom vroom!