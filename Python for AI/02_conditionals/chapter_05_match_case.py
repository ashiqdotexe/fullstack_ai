tea_type = input("Please select your tea type: (special, milk, normal, malai)").lower()
match tea_type:
    case "special": print(f"We will serve {tea_type}")