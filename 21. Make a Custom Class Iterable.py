# Define the custom exception
class InvalidAgeError(Exception):
    """Exception raised when age is below the minimum required age."""
    def __init__(self, age, message="Age must be at least 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Got: {self.age}"

# Function to check age
def check_age(age):
    """Check if age is valid (>= 18)."""
    if age < 18:
        raise InvalidAgeError(age)
    print(f"Valid age: {age}")

# Test the function with exception handling
def test_age_validation():
    test_ages = [15, 20, 17, 25, 16]
    
    for age in test_ages:
        try:
            print(f"\nTesting age {age}:")
            check_age(age)
        except InvalidAgeError as e:
            print(f"Error: {e}")
        else:
            print("Age accepted!")
        finally:
            print("Age check completed.")

# Run the tests
test_age_validation()