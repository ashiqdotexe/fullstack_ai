class TeaOrder:
    # The __init refers to constructor- means the class can accept parameter
    def __init__(self, type_, size): # Why we using "_" after "type" because type is a built in function
        self.size = size
        self.type = type_
    def order_now(self):
        return f"Now ordering {self.type} tea of size {self.size}ml"
    
my_tea = TeaOrder(type_="Masala", size=10)
print(my_tea.order_now())
        