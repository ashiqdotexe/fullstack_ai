def tea_shop():
    print("Welcome to the tea shop. Please place your order!")
    order = yield
    while True:
        print(f"Your {order} is being processed")
        order = yield

tea_order = tea_shop()
next(tea_order)
while True:
    ordering = input(f"\nWhat do you want to order: ")
    tea_order.send(ordering)
    decision = input(f"\nDo you want to order more? If yes then type 'y' or else type 'n': ")
    if decision.lower() == 'n':
        break