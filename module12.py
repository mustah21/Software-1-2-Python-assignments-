import json
import requests



#Task 1
server = "https://api.chucknorris.io/"
request = server + "/jokes/random"

try:
    response = requests.get(request).json()
    #print(json.dumps(response, indent=2))
    print(response["value"])
except requests.exceptions.RequestException as error:
    print("an error occurred")



#Task2
APIkey = "9bd3f3f913f212e19d8d63cf66b3a6fc"

try:
    def open_weather(x):
        server = "https://api.openweathermap.org/"
        req = f"{server}data/2.5/weather?q={city}&appid={APIkey}"
        response = requests.get(req)
        return response.status_code, response.json()

    def temp_celsius(kelvin):
        return kelvin - 273.15

    city = input("Enter city: ")
    status_code, weather_data = open_weather(city)

    if status_code == 200:
        kelvin_temp = weather_data['main']['temp']
        celsius_temp = temp_celsius(kelvin_temp)
        print(f"The temperature in {city} is {celsius_temp:.2f}°C.")

except requests.exceptions.RequestException as error:
        print("Error fetching data:")


