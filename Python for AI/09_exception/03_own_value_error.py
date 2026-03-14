def tea_serve(sugar, milk):
    if milk == 0 or sugar==0:
        raise ValueError("Please put the value of milk and sugar other than 0")
    print("Tea is ready")
tea_serve(2,3)