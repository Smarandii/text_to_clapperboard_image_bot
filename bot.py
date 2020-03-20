import telebot
import process

token = "951635447:AAG-OVmAtm9WMAOZ_HFRc0N0rfChzviweRY"
bot = telebot.TeleBot(token)
owner = 231584958


@bot.message_handler(commands=['start', 'donate', 'help'])
def start_message(message):
    if message.text == "/start":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJWHF5z4B5lNNi0tqyb8DLwXEiDe_3XAAJKKgACS2oDAAFgl8k4A3U_UxgE')
        bot.send_message(message.chat.id, 'Привет, дружок-пирожок!\nКогда нужна будет хлопушка, просто пиши мне данные в виде:\nВид работы, Название, ФИ, Группа, Хронометраж')
    elif message.text == '/donate':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJWH15z4WVkCRkcM34ux0fRa9zuxNoFAAKSAQAC9xyXApgQ4dZgui8TGAQ')
        bot.send_message(message.chat.id, 'Yandex.Money: 410012188653567\nSberbank: 5469380072221350')
        bot.send_message(owner, f'somebody pushed /donate button')
    elif message.text == '/help':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJWIl5z5KVtxXyQJgZogJS5RuXfpkUKAAKjAQAC9xyXAkQRNBGTUoaqGAQ')
        bot.send_message(message.chat.id, 'Когда нужна будет хлопушка, просто пиши мне данные в виде:\nВид работы, Название, ФИ, Группа, Хронометраж')


@bot.message_handler(content_types=['text'])
def send_text(message):
    message.text = process.formating(message.text)

    if process.check(message.text):
        bot.delete_message(message.chat.id, message.message_id)
        typeofw, name, fi, group, chron = message.text.split(",")
        process.create_image(typeofw, name, fi, group, chron)
        bot.send_photo(message.chat.id, open('result.jpg', 'rb'), caption=f'Твоя группа : {group.strip()}\nФамилия и Имя : {fi.strip()}\nНазвание твоей работы : {name.strip()}\nВид : {typeofw.strip()}\nХронометраж: {chron.strip()}')
    else:
        bot.send_message(message.chat.id, "❌ Что-то неверно, перепроверь ❌")
        bot.send_message(message.chat.id, 'Должно быть так : Вид работы, Название, ФИ, Группа, Хронометраж')


bot.polling()
