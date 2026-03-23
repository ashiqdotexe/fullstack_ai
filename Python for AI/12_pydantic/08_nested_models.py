from pydantic import BaseModel
class Adress(BaseModel):
    street : str 
    postal_code : str 
class User(BaseModel):
    name : str
    id: int 
    adress : Adress # Referencing to Adress class

user_1 = {
    "name" : "Ashiqur",
    "id" : 1,
    "adress" : {
        "street" : "123 street",
        "postal_code" : "A-1230"
    }
}
user = User(**user_1)
print(user)