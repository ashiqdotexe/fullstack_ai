from pydantic import BaseModel
from typing import Optional, List, Union

class Address(BaseModel):
    street : str 
    postal_code : str 
class Company(BaseModel):
    name : str
    address : Optional[Address] = None
class Person(BaseModel):
    name: str 
    company : Optional[Company] = None

person_1 = {
    "name" : "HM Ashiqur Rahman",
    "company" : {
        "name" : "Tocolabs",
        "address" : {
            "street" : "uttara dhaka",
            "postal_code" : "1230"
        }
    }
}
person = Person(**person_1)
print(person)