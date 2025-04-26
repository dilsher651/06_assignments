class A:
    def show(self):
        print("A's show()")

class B(A):
    def show(self):
        print("B's show()")

class C(A):
    def show(self):
        print("C's show()")

class D(B, C):  # Inherits from both B and C
    pass

# Create object and call show()
obj = D()
obj.show()  # Which show() gets called?

# Display Method Resolution Order
print("\nMethod Resolution Order (MRO):")
print(D.__mro__)