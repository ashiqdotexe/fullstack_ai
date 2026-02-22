# Integer and Float
total_milk = 10 
milk_served_in_cups = 3
milk_served = total_milk / milk_served_in_cups
print(f"Milk served- {milk_served}")
total_milk = 10 
milk_served_in_cups = 3
milk_served = total_milk // milk_served_in_cups # The double "/" causes the exact value
print(f"Milk served exact- {milk_served}")

#Boolean 
is_water_boiled = True
is_tea_added = False
can_tea_be_served = is_water_boiled and is_tea_added
if can_tea_be_served:
    print("yes")
else:
    print("no")