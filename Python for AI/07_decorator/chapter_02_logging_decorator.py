from functools import wraps

def logging_state(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        print(f"🚀 Starting {func.__name__}")
        func(*args, **kargs)
        print(f"✅ Finished {func.__name__}")
    return wrapper

@logging_state
def brew_tea(type, milk = "no"):
    print(f"Brewing {type} tea. Milk status {milk}")

brew_tea(type="Masala", milk="yes")