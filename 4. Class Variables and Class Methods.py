class Bank:
    bank_name = "Default Bank"  # Class variable shared by all instances

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name  # Modify the class variable

    def __init__(self, branch):
        self.branch = branch  # Instance variable

    def display_info(self):
        print(f"Bank: {Bank.bank_name}, Branch: {self.branch}")

# Create instances
bank1 = Bank("Downtown Branch")
bank2 = Bank("Uptown Branch")

# Before changing the bank name
print("Before change:")
bank1.display_info()  # Output: Bank: Default Bank, Branch: Downtown Branch
bank2.display_info()  # Output: Bank: Default Bank, Branch: Uptown Branch

# Change the bank name using the class method
Bank.change_bank_name("Global Bank")

# After changing the bank name
print("\nAfter change:")
bank1.display_info()  # Output: Bank: Global Bank, Branch: Downtown Branch
bank2.display_info()  # Output: Bank: Global Bank, Branch: Uptown Branch