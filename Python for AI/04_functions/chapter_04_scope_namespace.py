def tea_counter():
    tea_type = "Ginger" #Enclosed scope
    def tea_order():
        tea_type = "Masala" #Local Scope
        print(f"Inner: {tea_type}")
    tea_order()
    print(f"Inner: {tea_type}")
tea_type = "Tulsi" # Global Scope
tea_counter()
print(f"Global: {tea_type}")

