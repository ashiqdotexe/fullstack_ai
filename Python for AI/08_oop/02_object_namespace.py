class Tea:
    origin = "Bangladesh" # The variable inside class are called properties
# We can add properties to the class iteself
Tea.is_hot = True
print(Tea.origin)
print(Tea.is_hot)
# We can create object regarding the class and create properties using it, but it wont be added to the class itself
masala = Tea()
masala.flavour = "Cloves"
print(masala.flavour)
#print(Tea.flavour) # This won't work because its not a property of the class itself
masala.is_hot = False
print(f"Masala is hot? {masala.is_hot}")
print(f"Tea is hot? {Tea.is_hot}") # The value not getting change in the class itself
