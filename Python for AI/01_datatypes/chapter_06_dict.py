tea_order = dict(type="Black Tea", size = 2, sugar = "Less")
print(tea_order)
sugar = tea_order.get("sugar", "none") # Reading a particular item
print(sugar)
print(tea_order.items())
last_item = tea_order.popitem()
print(f"{last_item} removed from the dict")
print(tea_order)
for values in tea_order.values():
    print(values)
tea_first = {"type": "milk tea", "size": 2, "sugar": "2 cup"}
extra_ingredients = {"masla": ["Ginger", "Cardemom"]}
tea_first.update(extra_ingredients)
print(tea_first)