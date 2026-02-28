# Ternary operation
try:
    order_amount = int(input("Please enter your order amount: "))
    delivery_charge = 0 if order_amount > 300 else 30  # This is the ternary operation
    print(f"Delivery charge is: {delivery_charge} taka")
except Exception as e:
    print(f"Invalid Input. Error: {str(e)}")

