# 1. Define custom exception
class InvalidAgeError(Exception):
    """Raised when age is below 18"""
    pass

# 2. Function that raises the exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is below 18")
    print(f"Age {age} is valid")

# 3. Test with try-except
try:
    check_age(15)  # This will raise the exception
except InvalidAgeError as e:
    print(f"Error: {e}")  # Handle the custom exception
else:
    print("No errors occurred")
finally:
    print("Validation complete")

# Successful case
check_age(20)  # Output: "Age 20 is valid"