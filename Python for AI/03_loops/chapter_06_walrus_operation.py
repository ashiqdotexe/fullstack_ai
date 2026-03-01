# value = 13
# if(remainder:= value%5):
#     print(f"Value not divisible. Remainder is {remainder}")


# ":=" known as walrus 
available_flavours = ["masala", "malai", "lemon", "ginger"]
print(f"Available flavourse are {available_flavours}.")
while(flavour := input("Please select one flavour: ").lower()) not in available_flavours:
    print(f"The flavour- {flavour} isn't available. Please select another one")
print(f"You have selected {flavour} flavour")
sizes = ["large", "medium", "small"]
while(size := input(f"Please select the size. Available sizes are ({sizes}): ").lower()) not in sizes:
    print(f"{size} not available. Please try again..")
print(f"You have choosen {size}")