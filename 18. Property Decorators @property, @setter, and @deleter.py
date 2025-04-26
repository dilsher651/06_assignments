class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    @property
    def price(self):
        """Getter for price"""
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price"""
        print("Setting price...")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price

# Usage Example
product = Product("Laptop", 999.99)

# Get price (uses @property)
print(product.price)  # Output: Getting price... \n 999.99

# Set price (uses @price.setter)
product.price = 899.99  # Output: Setting price...

# Try invalid price
try:
    product.price = -100  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Price cannot be negative

# Delete price (uses @price.deleter)
del product.price  # Output: Deleting price...

# Verify deletion
print(hasattr(product, '_price'))  # Output: False