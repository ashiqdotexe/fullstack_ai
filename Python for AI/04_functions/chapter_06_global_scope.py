tea_type = "Milk"
def update_order():
    def kitchen():
        global tea_type
        tea_type = "Ginger"
    kitchen()
    print(f"After kitchen the tea type: {tea_type}")

update_order()