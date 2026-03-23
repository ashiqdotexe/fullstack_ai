from pydantic import BaseModel, field_validator, model_validator

class Person(BaseModel):
    first_name : str 
    last_name : str 
    @field_validator("first_name", "last_name") # Multiple field validation
    def name_capitilazation(cls, v):
        if not v.istitle():
            raise ValueError("Names must be in capital later")
        return v 
    
person = {
    "first_name" : "Ashiq",
    "last_name" : "Sohan"
}
person_1 = Person(**person)
print(person_1.model_dump())
    