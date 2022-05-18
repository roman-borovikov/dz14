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
        'name': 'roman',
        'age': 99
    }
    app.route("/")

    def index():
        #
        main_data = {

        }

        context = {
            'name': 'roman.borovikov',
            'age': 99
        }
    return render_template('index.html', main_data=main_data, **context)

@app.route('/contacts/')
def contacts():
    # где то взяли данные
    developer_name = 'Leo'
    # Контекст name=developer_name - те данные, которые мы передаем из view в шаблон
    # context = {'name': developer_name}
    # Словарь контекста context
    # return render_template('contacts.html', context=context)
    return render_template('contacts.html', name=developer_name, creation_date='16.01.2020')

    def contacts():
        # где то взяли данные
        developer_name = 'roman.borovikov'
        # Контекст name=developer_name - те данные, которые мы передаем из view в шаблон
        # context = {'name': developer_name}
        # Словарь контекста context
        # return render_template('contacts.html', context=context)
        return render_template('contacts.html', name=developer_name, creation_date='16.05.2022')

    @app.route('/results/')
    def results():
        data = ['python', 'js', 'java', 'sql', 'lua']
        # data = []
        return render_template('results.html', data=data)

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

