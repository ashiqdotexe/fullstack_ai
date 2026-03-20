from pydantic import BaseModel

class User(BaseModel):
    id: int
    name : str
    is_customer: bool

input_ = {"id" : 123, "name" : "sohan", "is_customer" : True}
user = User(**input_) # We have to use ** inorder to unpack the input
print(user)