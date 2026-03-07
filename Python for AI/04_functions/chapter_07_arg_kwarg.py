"""
When we dont know the argument that will be passed to the function we use args and kwarg.
"""
def make_tea(*ingredients, **extras):
    print(f"Ingredients are: {ingredients}")
    print(f"Extra ingredients are: {extras}")

make_tea("Tea", "Sugar", masala= ["ginger", "coriander"], flavour=["sweet", "extra sweet"])