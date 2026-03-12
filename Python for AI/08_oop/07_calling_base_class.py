# There are three ways how we can call the base class


class BaseTea:
    def __init__(self, type_, strenght):
        self.type = type_
        self.strenght = strenght

#1. Duplication
# class MyTea(BaseTea):
#     def __init__(self, type_, strenght, color):
#         # Rewrite everything of BaseTea
#         self.type = type_ 
#         self.strenght = strenght
#         self.color = color

#2. Explicit
# class MyTea(BaseTea):
#     def __init__(self, type_, strenght, color):
#         BaseTea.__init__(self,type_, strenght) #Explicitly calling the base class
#         self.color = color

#3. Super() method(Default)
class MyTea(BaseTea):
    def __init__(self, type_, strenght, color):
        super().__init__(type_, strenght)
        self.color = color
    def prepare(self):
        print(f"Preparing {self.type} tea of strenght- {self.strenght} and color- {self.color}")


my_tea = MyTea("Regular", "Strong", "Brown")
my_tea.prepare()