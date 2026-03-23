from pydantic import BaseModel, field_validator, model_validator

class Person(BaseModel):
    first_name : str 
    last_name : str 
    @field_validator("first_name", "last_name") # Multiple field validation
    def name_capitilazation(cls, v):
        if not v.istitle():
            raise ValueError("Names must be in capital later")
        return v 
    
class User(BaseModel):
    email : str
    @field_validator("email")
    def data_transformation(cls, v):
        return v.lower().strip()
    
person = {
    "first_name" : "Ashiq", #change it to "ashiq" to see the error
    "last_name" : "Sohan"
}
person_1 = Person(**person)
print(person_1.model_dump())
user = {
    "email" : "Ashiqur@bigibyte.com"
}
user_1 = User(**user)
print(user_1)

class Product(BaseModel):
    price : str # $4.44
    @field_validator("price")
    def datatype_converter(cls, v):
        if isinstance(v, str):
            return float(v.replace("$", ""))
        return v
product = {
    "price" : "$4.67"
} 
product_1 = Product(**product)
print(product_1)