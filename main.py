import telebot
from telebot import apihelper
import time
import os
import lxml

TOKEN = '5104499235:AAGjjITZrGPy8A_ooIdqxdrZoCTFSU2YYt8'

# Распарсить из статьи https://en.wikipedia.org/wiki/Bias-variance_tradeoff все заголовки верхнего уровня
import requests
import bs4

print('Новости по djano:')
req = requests.get('http://pythondigest.ru/feed/?q=django', verify=False)
print(req)
parser = bs4.BeautifulSoup(req.text, 'lxml')
# Выделим все заголовки четвертого уровня - тег h4:
y = parser.findAll('a', href=True, text=True)
with open('output.txt', 'wt') as f:
    for result in y:
        print('a tag', 'link_text', result['href'])
        f.write('a tag' + 'link_text' + result['href'])
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?here is django news enjoy!")
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Hhi, ")


# Обработка команд
@bot.message_handler(commands=['timer'])
def timer(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)


# Команда в параметром
@bot.message_handler(commands=['say'])
def say(message):
    # получить то что после команды
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, f'***{text.upper()}!***')


# Команда администратора
@bot.message_handler(commands=['admin'], func=lambda message: message.from_user.username == 'DanteOnline')
def admin(message):
    print(message)
    info = os.name
    bot.reply_to(message, info)


@bot.message_handler(commands=['admin2'])
def admin2(message):
    if message.from_user.username == 'DanteOnline':
        info = os.name
        bot.reply_to(message, info)
    else:
        bot.reply_to(message, 'Метод недоступен, нет прав')


@bot.message_handler(commands=['restart'])
def restart_server(message):
    # выполнить команду операционки из python
    # os.system('notepad')
    bot.reply_to(message, 'ура!')


@bot.message_handler(commands=['file'])
def get_file(message):
    print('зашел')
    # Передать какой то файл который есть на диске
    # with open('text.txt', 'r', encoding='utf-8') as data:
    #     bot.send_document(message.chat.id, data)
    with open('pict.jpg', 'rb') as data:
        bot.send_photo(message.chat.id, data)


@bot.message_handler(content_types=['text'])
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'В тексте слово плохой')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    FILE_ID = 'CAADAgADPQMAAsSraAsqUO_V6idDdBYE'
    bot.send_sticker(message.chat.id, FILE_ID)


bot.polling()

