def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")  # Log before calling
        return func(*args, **kwargs)      # Call the original function
    return wrapper

@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

# Test the decorated function
say_hello("Alice")