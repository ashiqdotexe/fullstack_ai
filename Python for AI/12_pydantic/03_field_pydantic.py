from pydantic import BaseModel
from typing import List, Dict, Optional

class Order(BaseModel):
    name : str
    items : List[str]
    quantities : Dict[str, int]
    is_payed : Optional[bool] = False

order = Order(name="Sohan", items=["Tea", "Toast"], quantities={"Tea": 1, "Toast": 3}, is_payed=True)
print(order)