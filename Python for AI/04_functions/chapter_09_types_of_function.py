# Pure functions
def pure_tea(cups):
    return cups
#impure function-> Not recommended
total_cups = 10
def impure_tea(cups):
    global total_cups
    total_cups+=cups
    return total_cups

#Recursive function
def recursive_tea(cups):
    if cups == 0:
        return "All cups been processed"
    print(f"Currently processing {cups} cups")
    return recursive_tea(cups-1) # iterative recursion
print(recursive_tea(3))

#Lambda function(anonnymous)
tea_list = ["light", "strong", "strong", "ginger", "milk"]
strong_tea = list(filter(lambda tea: tea=="strong", tea_list)) # lambda here works like a function(small kinda function without any particular name, "tea works as a variable here")
print(strong_tea)