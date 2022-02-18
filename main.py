# Распарсить из статьи https://en.wikipedia.org/wiki/Bias-variance_tradeoff все заголовки верхнего уровня
import requests
import bs4
req = requests.get('http://pythondigest.ru/feed/?q=django', verify = False)
print(req)
parser = bs4.BeautifulSoup(req.text, 'lxml')
#Выделим все заголовки четвертого уровня - тег h4:
y = parser.findAll('a')
for result in y:
    print('h1 tag',result.text)