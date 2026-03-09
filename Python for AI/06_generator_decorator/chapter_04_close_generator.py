# Importing other generator or subgenerator using yield

def desi_tea():
    yield "Milk tea"
    yield "Raw tea"
def imported_tea():
    yield "Matcha"
    yield "Oloong"
def full_menu():
    yield from desi_tea()
    yield from imported_tea()

menu = full_menu()
for tea in menu:
    print(tea)

def tea_stall():
    try:
        while True:
            order = yield "Please give your order"
    except:
        print(f"Tea stall closed")

tea_order = tea_stall()
print(next(tea_stall()))
tea_order.close() # Cleaning up the memory