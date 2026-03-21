from pydantic import BaseModel, field_validator, model_validator
from typing_extensions import Self
class User(BaseModel):
    username : str
    @field_validator("username") # We use field validator for only one field. e.g- username or password or any one field
    def username_check(cls, v):
        if len(v) < 4:
            raise ValueError("The username must be of 5 characters")
        return v 
class Password(BaseModel):
    password : str
    confirm_password : str
    @model_validator(mode="after") # We use model validator for whole class.. The mode = "after" checks all the datatype of each field and then proceeds
    def check_password(self)-> Self:
        if self.password != self.confirm_password:
            raise ValueError("Password didn't match")
        return self

user = {
    "username" : "HM Ashiqur"
}
password = {
    "password": "sohan",
    "confirm_password" : "sohan"
}
user_ = User(**user)
pass_ = Password(**password)
print(user_)
print(pass_)