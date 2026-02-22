tea_ingredient = ["water", "milk", "black tea"]
tea_ingredient.append("sugar")
print(f"Tea ingredients are-> {tea_ingredient}")
masala_ingredients = ["cardemom", "ginger"]
tea_ingredient.extend(masala_ingredients)
print(f"Tea ingredients are-> {tea_ingredient}")
tea_ingredient.insert(2,"coffee")
print(f"Tea ingredients are-> {tea_ingredient}")
last_ingredient = tea_ingredient.pop()
print(f"{tea_ingredient}. {last_ingredient} removed from the list!")
print(last_ingredient)
tea_ingredient.append(last_ingredient)
print(f"{tea_ingredient}. {last_ingredient} added to the list again!")
sugar_per_cup = [1,3,4,5,2]
print(f"Max is: {max(sugar_per_cup)} and Min is: {min(sugar_per_cup)}")
# Different way to find the max and min->
print("Different way to find the max and min->")
temp = sugar_per_cup[:]
sugar_per_cup.sort() # 1 2 3 4 5 
max_value = sugar_per_cup.pop()
print(f"Max is: {max_value}")
sugar_per_cup.reverse() # 4 3 2 1
min_value = sugar_per_cup.pop()
print(f"Min is: {max_value}")
print(temp)
print(f"Memory id of sugar {id(sugar_per_cup)}")
print(f"Memory id of temp {id(temp)}")

