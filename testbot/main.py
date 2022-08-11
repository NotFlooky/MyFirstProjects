import telebot

bot= telebot.TeleBot('5592756427:AAEyROvQC2PdjJr7DMoFA2wRI5fgiI7IEmw')


@bot.message_handler(commands=["start","update"])
def start(message):
    if message.text=="/start":
        bot.send_message(message.chat.id,'<b>Привет! Я бот, который может вывести всю информацию о тебе! Просто напиши\
     какую информацию своего профиля ты хочешь узнать.</b>(Имя, Фамилия, ID, Никнейм)',parse_mode='html')
    elif message.text=="/update":
        bot.send_message(message.chat.id, '<b><em>Разработкой данного бота занимался @flookylox. Обновления будут,\
но не особо часто :)</em></b> ', parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text=="Имя":
        bot.send_message(message.chat.id,f'Твое имя:<b> {message.from_user.first_name}</b>',parse_mode='html')
    elif message.text=="Фамилия":
        bot.send_message(message.chat.id, f'Твоя фамилия:<b> {message.from_user.last_name}</b>', parse_mode='html')
    elif message.text=="ID":
        bot.send_message(message.chat.id, f'Твое ID:<b> {message.from_user.id}</b>', parse_mode='html')
    elif message.text=="Никнейм":
        bot.send_message(message.chat.id, f'Твой никнейм:<b>{message.from_user.username}</b>', parse_mode='html')
    else:
        bot.send_message(message.chat.id, '<b>Ты ввёл несуществующий параметр!</b>',parse_mode='html')


@bot.message_handler(commands=['update'])
def update(message):
    bot.send_message(message.chat.id,'<b><em>Разработкой данного бота занимался @flookylox. Обновления будут, \
    но не особо часто :)</b></em> ', parse_mode='html')


bot.polling(none_stop=True)