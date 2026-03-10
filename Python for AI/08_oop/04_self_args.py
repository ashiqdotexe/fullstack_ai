class Tea:
    size = 150 #ml
    def serve(self): # When a function is called inside a class then its called method
        return f"Serving {self.size}ml of tea"

my_tea = Tea()
# print(my_tea.serve())
# if we call it directly through the class then we must provide the object as well
print(Tea.serve(my_tea)) # we must provide the object itself as well
my_tea_two = Tea()
my_tea_two.size = 100
print(Tea.serve(my_tea_two)) 