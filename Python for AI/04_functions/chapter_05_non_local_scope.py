def update_order():
    tea_type = "coriander"
    def ketchen():
        nonlocal tea_type #non local-> calling variable within the function
        tea_type = "ginger"
    ketchen()
    print("After kitche, tea type update: ", tea_type)
update_order()