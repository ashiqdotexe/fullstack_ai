from functools import wraps
def required_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Denied")
            return None
        else:
            func(user_role)
    return wrapper

@required_admin
def access_tea_stall(user_role):
    print("Access granted")

access_tea_stall("user")
access_tea_stall("admin")