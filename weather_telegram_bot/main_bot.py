import requests
import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime


weather_token = config.open_weather_token
token= config.tg_bot_token
bot= Bot(token=token)
dp= Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r= requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric"
        )
        data= r.json()

        city=data['name']
        cur_weather=data["main"]["temp"]
        humidity = data["main"]["humidity"]
        speed=data['wind']['speed']
        sunrise_time=datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time=datetime.datetime.fromtimestamp(data['sys']['sunset'])

        await message.reply(f'***{datetime.datetime.now().strftime("%Y-%m-%d %H:%m")}*** \n'
              f"Погода в городе : {city} \nТемпература : {cur_weather}С° \n"
              f"Влажность : {humidity} \nСкорость ветра: {speed}м/с \nВремя восхода солнца : {sunrise_time} \n"
              f"Время захода солнца : {sunset_time} \n Хорошего дня :)")
    except:
        await message.reply("Проверьте название города \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)