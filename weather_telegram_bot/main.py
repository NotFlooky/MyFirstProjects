import config
from pprint import pprint
import requests
import datetime

token= config.open_weather_token

def get_weather(city, token):
    try:
        r= requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"
        )
        data= r.json()

        city=data['name']
        cur_weather=data["main"]["temp"]
        humidity = data["main"]["humidity"]
        speed=data['wind']['speed']
        sunrise_time=datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time=datetime.datetime.fromtimestamp(data['sys']['sunset'])

        print(f'***{datetime.datetime.now().strftime("%Y-%m-%d %H:%m")}*** \n'
              f"Погода в городе : {city} \nТемпература : {cur_weather}С° \n"
              f"Влажность : {humidity} \nСкорость ветра: {speed}м/с \nВремя восхода солнца : {sunrise_time} \n"
              f"Время захода солнца : {sunset_time} \n Хорошего дня :)")
    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city=input('Введите название города:')
    get_weather(city, token)


if __name__ == "__main__":
    main()
