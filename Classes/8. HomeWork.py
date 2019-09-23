'''Восьмое задание. Получить список статей хабра за месяц.
https://habr.com/top/monthly/'''



import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text


def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	h1 = soup.find('div', class = "tabs__level tabs__level_bottom").find('li' class = "toggle-menu__item").find('a href' ="https://habr.com/ru/top/monthly/" class="toggle-menu__item-link toggle-menu__item-link_active" rel="nofollow" title="Лучшие публикации за месяц")
	return h1


def main():
	url = 'https://habr.com/ru/top/monthly/'
	print(get_data(get_html(url)))
main()