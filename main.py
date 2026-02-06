import requests
from twilio.rest import Client

account_sid = "AC738b9b5400b1db77ee1f905a915a0ff8"
auth_token = "d65fe8a9d333a47321ccac5d63a4ca82"
client = Client(account_sid, auth_token)

api_key = "cc64f27ff000ae8d4fcb94cf349600e4"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat":-26.1,
    "lon":27.8,
    "appid": api_key,
    "cnt":4
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)

data = response.json()
weather_data = [condition["weather"][0]["id"] for condition in data["list"]]

will_rain = False
for condition in weather_data:
    if condition < 700:
        will_rain = True
        break

if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella☔.",
        from_="+17156438083",
        to="+27670873126",
    )

    print(message.status)