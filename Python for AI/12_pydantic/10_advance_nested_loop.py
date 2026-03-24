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

# Mixing up data type
class TextContent(BaseModel):
    type : str = "Text content"
    content : str 
class ImageContent(BaseModel):
    type : str = "Image content"
    image_url : str 
    alt_text : Optional[str] = None 
class WebContent(BaseModel):
    title : str 
    section : Optional[List[Union[TextContent, ImageContent]]] = None

webcontent_1 = {
    "title" : "Tocolabs web",
    "section" : [{
        "content" : "This is the website"
    },
    {
        "image_url" : "this is the url"
    }
    ]
}
web = WebContent(**webcontent_1)
print(web) 