import requests

def get_weather(city: str):
    response = requests.get(f"https://wttr.in/{city.lower()}?format=j1")
    data = response.json()
    current_weather = data.get("current_condition", {})[0].get("temp_C", {})
    return current_weather
print(get_weather("Khulna"))