class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start(self):
        print(f"{self.engine_type} engine started. Vroom vroom!")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Car "has-a" Engine
    
    def start_car(self):
        print(f"Starting {self.brand} car...")
        self.engine.start()  # Accessing Engine's method

# Create an Engine object
v8_engine = Engine("V8")

# Create a Car object with the Engine
mustang = Car("Ford Mustang", v8_engine)

# Start the car (which uses the engine)
mustang.start_car()