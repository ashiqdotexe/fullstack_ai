class Tea:
    origin = "Bangladesh"
    cup = 2

my_tea = Tea()
print(f"My tea cup before changing {my_tea.cup}")
my_tea.cup = 3
print(f"My tea cup before changing {my_tea.cup}")
#Now What if I delete the the cup that I just changed?
del my_tea.cup
print(f"My tea cup before changing {my_tea.cup}") # it falls back to the original class. This is called attribute shadowing
#now what if I create a new thing that doesnt exist in the original class? And then delete it
my_tea.size = 4
print(f"My cup size before deleting {my_tea.size}")
del my_tea.size 
try:
    print(my_tea.size)
except:
    print("Can't print the size because it has already been deleted and not present in the original class as well")

