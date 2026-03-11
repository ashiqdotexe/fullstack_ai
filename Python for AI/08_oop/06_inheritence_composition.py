class BaseTea:
    def __init__(self, type_):
        self.type = type_
    def prepare(self):
        print(self.type)

class MasalaTea(BaseTea):
    def add_masala(self):
        return f"Adding masala like cardamom, ginger on {self.type} tea"

tea_making = MasalaTea("masala")
print(tea_making.add_masala())