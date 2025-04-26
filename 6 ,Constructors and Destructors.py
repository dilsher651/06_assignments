class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Logger object '{self.name}' created.")  # Constructor message

    def __del__(self):
        print(f"Logger object '{self.name}' destroyed.")  # Destructor message

# Example usage
def test():
    print("--- Start of scope ---")
    logger = Logger("TestLogger")  # Constructor runs
    print("--- End of scope ---")
    # Destructor runs automatically when `logger` goes out of scope

test()  # Call the function to see constructor/destructor in action

# Optional: Force garbage collection to see destructor message immediately
import gc
gc.collect()