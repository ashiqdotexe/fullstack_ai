"""
Function returns value at once. Generator yield the value and return when it gets called
"""

def get_tea_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

get_tea_1 = get_tea_list()
print(f"Memory <{id(get_tea_1)}> accured by {get_tea_1}")
print(get_tea_1)

def get_tea_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"
print(f"Generator-->")
get_tea_2 = get_tea_gen()
print(f"{next(get_tea_2)}")
print(f"{next(get_tea_2)}")
print(f"{next(get_tea_2)}")