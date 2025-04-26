class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name       # Public variable (no underscore)
        self._salary = salary   # Protected variable (single underscore)
        self.__ssn = ssn       # Private variable (double underscore)

# Create an object
emp = Employee("Alice", 75000, "123-45-6789")

# Accessing variables from outside the class:
print("Public (name):", emp.name)        # Works ✅
print("Protected (_salary):", emp._salary)  # Works but discouraged (convention) ⚠️
print("Private (__ssn):", emp.__ssn)     # Fails ❌ (AttributeError)