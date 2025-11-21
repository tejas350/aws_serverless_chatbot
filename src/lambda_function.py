
import json
import requests

def lambda_handler(event, context):
    city = event['sessionState']['intent']['slots']['city']['value']['interpretedValue']
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    result = requests.get(url).json()
    temperature = result['main']['temp'] - 273.15

    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {"name": "GetWeatherInfo", "state": "Fulfilled"}
        },
        "messages": [{
            "contentType": "PlainText",
            "content": f"The temperature in {city} is {temperature:.2f}°C."
        }]
    }
