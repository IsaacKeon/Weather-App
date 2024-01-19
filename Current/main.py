import requests

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

api_key = open('api_key','r').read()

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404': 
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    celsius = fahrenheit_to_celsius(temp)

    print(f"The weather in {user_input} is : {weather}")
    print(f"The tempature in {user_input} is : {celsius} celsius")

