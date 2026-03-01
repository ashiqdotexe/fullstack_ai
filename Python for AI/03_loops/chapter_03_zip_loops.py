names = ["Ashiq", "Adnan", "Sohan", "Rohan"]
bills = [50, 100, 70, 55]
for name, amount in zip(names, bills):
    print(f"Bill for {name} is {amount} taka")