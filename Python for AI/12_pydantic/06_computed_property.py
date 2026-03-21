from pydantic import BaseModel, computed_field


class OrderPrice(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property  # when we use this, the function next to it becomes the property of the class itself
    def calculated_price(self) -> float:
        return self.price * self.quantity


order_price = OrderPrice(price=297.7, quantity=2)
print(f"The price is {order_price.calculated_price}")
# To see the whole thing inside the class we can use modeldump()
print(
    order_price.model_dump()
)  # You will see that the "calculated_price" itself has become a property of the class itself alongside with price and quantity
