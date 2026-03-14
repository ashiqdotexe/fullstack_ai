class OrderOutOfIngredients(Exception):
    pass
def tea_order(item):
    if item not in ["masala", "ginger", "milk"]:
        raise OrderOutOfIngredients(f"The item- {item} is not available")
    print(f"Preparing {item} tea.....")

tea_order("mint")