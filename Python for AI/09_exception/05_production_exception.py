class CustomException(Exception): pass
def tea_order(item, amount):
    try:
        menu = {"masala": 20, "ginger": 40}
        if item not in menu:
            raise CustomException(f"The item- {item} not available")
        if not isinstance(amount, int):
            raise TypeError("Please enter a valid amount")
        total = menu[item] * amount
        print(f"Your total bill for {item} item of {amount} amount is {total}")
    except Exception as e:
        print("Error", e)

tea_order("mint", 2)
tea_order("masala", "three")
tea_order("ginger", 2)
        