class TeaLeaf:
    def __init__(self, age):
        self._age = age
    # getter method
    @property
    def age(self):
        return self._age
    # setter
    @age.setter
    def age(self, age):
        if 1<= age <= 5:
            self._age = age
        else:
            raise ValueError("must be in between 1 and 5")

quality = TeaLeaf(4)
print(quality.age) 
quality.age = 3
print(quality.age) 