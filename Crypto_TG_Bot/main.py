import requests
from datetime import datetime

import telebot

bot_token= "5642048444:AAH1GqD0oCm3tsksB-ea_p_hiGhkm0zd1U4"

def get_data_xrp():
    req= requests.get('https://yobit.net/api/3/ticker/xrp_usd')
    response = req.json()
    sell_xrp_price = response["xrp_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell XRP price:{sell_xrp_price}")
def get_data_btc():
    req= requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    sell_btc_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price:{sell_btc_price}")

def get_data_eth():
    req = requests.get('https://yobit.net/api/3/ticker/eth_usd')
    response = req.json()
    sell_eth_price = response["eth_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ETH price:{sell_eth_price}")
def get_data_usdc():
    req= requests.get('https://yobit.net/api/3/ticker/usdc_usd')
    response = req.json()
    sell_usdc_price = response["usdc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell USDC price:{sell_usdc_price}")
def get_data_usdt():
    req= requests.get('https://yobit.net/api/3/ticker/usdt_usd')
    response = req.json()
    sell_usdt_price = response["usdt_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell USDT price:{sell_usdt_price}")
def get_data_bnb():
    req= requests.get('https://yobit.net/api/3/ticker/bnb_usd')
    response = req.json()
    sell_bnb_price = response["bnb_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BNB price:{sell_bnb_price}")
def get_data_busd():
    req= requests.get('https://yobit.net/api/3/ticker/busd_usd')
    response = req.json()
    sell_busd_price = response["busd_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BUSD price:{sell_busd_price}")
def get_data_ada():
    req= requests.get('https://yobit.net/api/3/ticker/ada_usd')
    response = req.json()
    sell_ada_price = response["ada_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ADA price:{sell_ada_price}")
def get_data_sol():
    req= requests.get('https://yobit.net/api/3/ticker/sol_usd')
    response = req.json()
    sell_sol_price = response["sol_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell SOL price:{sell_sol_price}")
def get_data_doge():
    req= requests.get('https://yobit.net/api/3/ticker/doge_usd')
    response = req.json()
    sell_doge_price = response["doge"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell DOGE price:{sell_doge_price}")



bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,'Hello, my friend!Enter the name of the cryptocurrency and I will display the price of this cryptocurrency(BTC, ETH, USDT, USDC, BNB, XPR, BUSD, ADA, SQL, DOGE)' )

@bot.message_handler()
def get_data_user(message):
    if message.text == 'BTC':
        req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
        response = req.json()
        sell_btc_price = response["btc_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price:{sell_btc_price}"+"$")
                )
    elif message.text == "ETH":
        req = requests.get('https://yobit.net/api/3/ticker/eth_usd')
        response = req.json()
        sell_eth_price = response["eth_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ETH price:{sell_eth_price}"+"$")
                )
    elif message.text == "USDC":
        req = requests.get('https://yobit.net/api/3/ticker/usdc_usd')
        response = req.json()
        sell_usdc_price = response["usdc_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell USDC price:{sell_usdc_price}"+"$")
                )
    elif message.text == "XRP":
        req = requests.get('https://yobit.net/api/3/ticker/xrp_usd')
        response = req.json()
        sell_xrp_price = response["xrp_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell XRP price:{sell_xrp_price}"+"$")
                )
    elif message.text == "USDT":
        req = requests.get('https://yobit.net/api/3/ticker/usdt_usd')
        response = req.json()
        sell_usdt_price = response["usdt_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell USDT price:{sell_usdt_price}"+"$")
                )
    elif message.text == "BNB":
        req = requests.get('https://yobit.net/api/3/ticker/bnb_usd')
        response = req.json()
        sell_bnb_price = response["bnb_usd"]["sell"]
        bot.send_message(
            message.chat.id
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BNB price:{sell_bnb_price}"+"$")
                )
    elif message.text == "BUSD":
        req = requests.get('https://yobit.net/api/3/ticker/busd_usd')
        response = req.json()
        sell_busd_price = response["busd_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BUSD price:{sell_busd_price}"+"$")
                )
    elif message.text == "ADA":
        req = requests.get('https://yobit.net/api/3/ticker/ada_usd')
        response = req.json()
        sell_ada_price = response["ada_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell ADA price:{sell_ada_price}"+"$")
               )
    elif message.text == "SQL":
        req = requests.get('https://yobit.net/api/3/ticker/sql_usd')
        response = req.json()
        sell_sql_price = response["sql_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell SQL price:{sell_sql_price}"+"$")
                )
    elif message.text == "DOGE":
        req = requests.get('https://yobit.net/api/3/ticker/doge_usd')
        response = req.json()
        sell_doge_price = response["doge_usd"]["sell"]
        bot.send_message(
            message.chat.id,
            (f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell DOGE price:{sell_doge_price}"+"$")
                )









    else:
        bot.send_message(message.chat.id,"Sorry, but so far there is no such cryptocurrency in my functionality")


if __name__ == "__main__":
    bot.polling()
