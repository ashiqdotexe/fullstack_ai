suger_amount = 2
print(f"Initial sugar: {suger_amount}")

suger_amount = 12
print(f"Initial sugar: {suger_amount}")

"""
Values are immutable which means even if we change the value the initial value remains in the memory... so its immutable
"""

print(f"The id of 2 is: {id(2)}")
print(f"The id of 12 is: {id(12)}")


""""
There are some mutable value as well. For example "set()" is mutable... Even if we add values to set, the id never changes(remains the same) 

"""

spice_mix = set()
print(f"The id of spice_mix is {id(spice_mix)}")
spice_mix.add("cardemom")
spice_mix.add("cinnamon")
print(f"The id of spice mix is {id(spice_mix)}")