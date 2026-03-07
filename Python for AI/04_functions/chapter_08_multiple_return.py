def tota_sales():
    return 100 ,10, 20

total, paid, _ = tota_sales()
print(f"Total sales {total}")
print(f"Paid {paid}")

def total_order(order):
    if order == 0:
        return "Ordered nothing"
    return f"Ordered {order} tea. processing"

print(total_order(0))
print(total_order(5))