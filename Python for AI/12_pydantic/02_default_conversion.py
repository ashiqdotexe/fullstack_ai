from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True # We can give default value as well

product_one = Product(id=1, name = "Laptop", price=29.99, in_stock=False)