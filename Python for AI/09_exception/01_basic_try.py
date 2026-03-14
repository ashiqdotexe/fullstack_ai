def serve(tea_type):
    try:
        if tea_type.lower() == "unknown":
            raise ValueError(f"We don't have that flavor {tea_type}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"{tea_type} served")
    finally:
        print("Next customer please")

serve("masala")
serve("Unknown")