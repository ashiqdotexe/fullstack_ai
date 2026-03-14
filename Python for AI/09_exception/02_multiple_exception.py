def tea_order(item, amount):
    try:
        price = {"masala":20}[item]
        cost = int(price * amount)
        print(f"The price of the tea is {cost}")
    except ValueError:
        print(f"The type of {item} is not available")
    except KeyError:
        print(f"The type of {item} is not available")
    except TypeError:
        print(f"Please give a valid input")
tea_order("mint", 2)
tea_order("masala", None)