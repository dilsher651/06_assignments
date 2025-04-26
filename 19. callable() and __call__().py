class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor
    
    def __call__(self, x):
        """Makes the object callable like a function"""
        return x * self.factor

# Testing
mult_by_5 = Multiplier(5)

# 1. Verify it's callable
print(callable(mult_by_5))  # Output: True

# 2. Call the object like a function
print(mult_by_5(10))  # Output: 50 (10 * 5)
print(mult_by_5(7))   # Output: 35 (7 * 5)

# 3. Create another multiplier
mult_by_neg2 = Multiplier(-2)
print(mult_by_neg2(8))  # Output: -16 (8 * -2)