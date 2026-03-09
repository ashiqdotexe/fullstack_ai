from functools import wraps

def statement(func):
    @wraps(func) # We are using this because it preserves the original function's metada
    def wrapper():
        print(f"Before running the function")
        func()
        print(f"After running the function")
    return wrapper

@statement
def simple_function():
    print("Simple function")

simple_function()

print(simple_function.__name__) # If we dont use @wraps(func), it will print wrapper function