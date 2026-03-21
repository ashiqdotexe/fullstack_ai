from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class User(BaseModel):
    name : str = Field(
        ..., # These three dots means these fields are mandatory
        min_length= 3,
        max_length= 50,
        description= "User name",
        examples= "HM Ashiqur Rahman",   
    )
    salary : float = Field(
        ...,
        ge = 10000, # These ge, le ,gt, lt means greater than equal, less than... and so on 
        le = 1000000,
        description= "This is the annual year salary"  
     )

user_data_1 = {
    "name" : "HM Adnanur Rahman",
    "salary" : 10000.202
}
user_1 = User(**user_data_1)
print(f"Employee name is {user_1.name} and his salary is {user_1.salary}")