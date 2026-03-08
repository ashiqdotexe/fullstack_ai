def total_bill(cups = 0, snacks = 0):
    """
    This function generate the total bill

    :params: cups- by default 0 cups and per cups cost 10 taka
    :params: snack- by default 0 snack and per snacks cost 15 taka
    :return total_bill and thank you message as string
    """
    # The documentation comment should always be in the very first of a function
    total = cups*10 + snacks*15
    return total, "Thank you for ordering"

bill, message = total_bill(cups=2, snacks=3)
print(f"Total bill is {bill}. {message}")

# The "--" double underscore is called Dunder. So when we call doc- its called dunderdoc
print(total_bill.__doc__)
print(f"Function name is {total_bill.__name__}")