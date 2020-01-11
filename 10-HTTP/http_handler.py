"""Для корректного запуска программы необходимо
 авторизироваться на сайте pikabu.ru, после этого получить вам cookie
 из get запроса на pikabu.ru к файлу /, а именно скопировать строку Cookie
  и вставить их в файл cookies.txt.
   После данных действий программа должна успешно выполниться"""
import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


def get_posts(text, s):
    for i in range(1, 11):
        response = s.get(f'https://pikabu.ru/hot/subs/actual?page={i}', headers=HEADERS)
        text.append(response.text)


def get_popular_tags(text):
    top = {}
    html = BeautifulSoup(''.join(text), 'html.parser')
    tags = [tag.get_text() for tag in html.find_all('a', {'data-tag': True})]
    for i in set(tags):
        top.update({i: tags.count(i)})
    top = list(top.items())
    top = sorted(top, key=lambda i: i[1], reverse=True)[:10]
    print('\tTop 10 tags'.upper())
    for i in top:
        print(f'{i[0]} - {i[1]}')


if __name__ == '__main__':
    s = requests.Session()
    with open('./cookies.txt') as file:
        cookies = file.read()
        HEADERS['Cookie'] = cookies.strip()
    text = []
    get_posts(text, s)
    get_popular_tags(text)
    s.close()
