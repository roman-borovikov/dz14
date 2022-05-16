from flask import Flask, render_template, request
app = Flask(__name__)
app = Flask(__name__)
#import telebot
#from telebot import apihelper
import time
import os
#import lxml
import requests
#import bs4
@app.route("/")
def index():

    main_data = {
        'a': 'A',
        'b': 'B',
        'c': 'C'
    }

    context = {
        'name': 'Leo',
        'age': 99
    }
    app.route("/")

    def index():
        #
        main_data = {
            'a': 'A',
            'b': 'B',
            'c': 'C'
        }

        context = {
            'name': 'Leo',
            'age': 99
        }
    return render_template('index.html', main_data=main_data, **context)
    # return render_template('index.html', main_data=main_data, name='Leo', age=99)
print('Новости по djano:')
req = requests.get('http://pythondigest.ru/feed/?q=django', verify=False)
print(req)
#parser = bs4.BeautifulSoup(req.text, 'lxml')
# Выделим все заголовки четвертого уровня - тег h4:



TOKEN = '5104499235:AAGjjITZrGPy8A_ooIdqxdrZoCTFSU2YYt8'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

# Информация о боте
url = f'{MAIN_URL}/getMe'

print(url)








if __name__ == "__main__":
    app.run(debug=True)

