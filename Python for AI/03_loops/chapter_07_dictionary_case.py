users = [
    {"id" : 1, "total": 150, "coupon" : "P10"},
    {"id" : 2, "total": 200, "coupon" : "P20"},
    {"id" : 3, "total": 100, "coupon" : "F10"}
]
discounts = {
    "P10" : (0.2, 0),
    "P20" : (0.5, 0),
    "F10" : (0, 10)
}
for user in users:
    percentage, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percentage + fixed
    print(f"User with id- #{user["id"]} paid {user["total"]} taka so he will recieve a discount of {discount} taka")