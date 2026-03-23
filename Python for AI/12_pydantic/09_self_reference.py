from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id : int
    content : str 
    replies : Optional[List["Comment"]] = None # Self referencing
Comment.model_rebuild() # Forward referencing. Must include after self refrencing

user_comment = {
    "id" : 1,
    "content" : "comment-1",
    "replies": [
        {
            "id" : 2,
            "content" : "comment-2"
        },
        {
            "id" : 3,
            "content" : "comment-3",
            "replies" : [
                {
                "id" : 1,
                "content" : "nested comment"
                }
            ]
        }
    ]
}
user = Comment(**user_comment)
print(user)