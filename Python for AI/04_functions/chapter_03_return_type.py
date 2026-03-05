def add_vat(price, vat_rate):
    return price * (100+vat_rate)/100
orders = [100, 150, 200]
for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Actual price is {price}. Final amount after adding vat is {final_amount}")