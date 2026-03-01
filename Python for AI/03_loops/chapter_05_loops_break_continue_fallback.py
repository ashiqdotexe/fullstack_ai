canditates = [("Ashiq", 17), ("Adnan", 13), ("sohan",18), ("rohan", 14)]
for canditate, age in canditates:
    if age < 14:
        print(f"The canditate- {canditate} is underage as his age is {age}")
        continue
    if age >= 18:
        print(f"The canditate- {canditate} is suitable for the position as his age is {age}. Stopping hiring process here")
        break
else: 
    print("No canditate founds!") # Fallback