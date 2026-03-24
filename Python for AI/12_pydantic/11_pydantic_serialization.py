from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class Address(BaseModel):
    street : str
    postal_code : str 
class User(BaseModel):
    name : str
    created_at : datetime
    address : Address
    tags : Optional[List[str]]

    model_config = ConfigDict(
        json_encoders= {
            datetime : lambda x : x.strftime("%Y-%m-%d %H:%M:%S")
        }
    )

user_1 = {
    "name" : "Ashiqur",
    "created_at" : datetime(2025, 5, 24, 4, 20, 45),
    "address" :{
        "street": "uttara dhaka",
        "postal_code" : "200121"
    },
    "tags" : ["Subscriber", "Premium"]
}
user = User(**user_1)
print(user) # Normal printing
print("="*30)    