class BaseTea:
    def __init__(self, tea_type, strength, size):
        self.tea_type = tea_type
        self.strength =strength
        self.size = size
    # The user can give dictionary instead for that reason we will use classmethod to handle that as well
    @classmethod
    def from_dict(cls, order_dict):
        return cls(
            order_dict["tea_type"],
            order_dict["strength"],
            order_dict["size"]
        )
    # The user can give string as well. We have to handle them as wwell
    def from_string(cls, order_string):
        tea_type, strength, size = order_string.split("-")
        return cls(tea_type, strength, size)

# calling dictionary
dict_ = BaseTea.from_dict(
    {
        "tea_type" : "masala",
        "strength" : "strong",
        "size" : "medium"
    }
)
print(dict_.__dict__)
        