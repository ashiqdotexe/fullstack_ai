import time
class BaseTea:
    def __init__(self, type_):
        self.type = type_
    def prepare(self):
        print(f"Preparing {self.type} tea.....")

class MasalaTea(BaseTea):
    def add_masala(self):
        print(f"Adding masala to {self.type} tea...")

class TeaStall:
    tea_shop = BaseTea # calling a class without the parenthesis "()" is called Composition, we might call it in the later part thats why we didnt mention the parenthesis

    def __init__(self, snack):
        self.tea_object = self.tea_shop("Regular") # Now we are calling it and refrencing the object to "tea_object". So from now on the tea_object will hold the object itself
        self.snack = snack
    def serve(self):
        print(f"Serving {self.tea_object.type} tea with {self.snack} snacks")
class FancyStall(MasalaTea):
    fancy_stall = TeaStall # We are both inheriting and compositioning in the same class here


shop = TeaStall("Busicket")
shop.tea_object.prepare()
time.sleep(3)
fancy = FancyStall("Regular")
fancy.add_masala()
time.sleep(3)
shop.serve()
