# Nested if else condition

device_status_choose = input("Please choose an option:\n1. Active\n2. Inactive\n:")
device_status = ""
if device_status_choose == "1": device_status = "active"
elif device_status_choose == "2" : device_status == "inactive"
else: print("Invalid input")

if device_status == "active":
    temparature = int(input("Please enter the temparature: "))
    if temparature > 35:
        print("Alert!! Temparature is high.")
    else:
        print("Temparature is low")
else:
    print("Device is Inactive")