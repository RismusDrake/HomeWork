'''Восьмое задание. Получить список статей хабра за месяц.
https://habr.com/top/monthly/'''



import requests
from bs4 import BeautifulSoup

def get_html(url):
	r = requests.get(url)
	return r.text

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	h1 = soup.find('link', title = 'Лучшие публикации за месяц').text

def main():
	url = 'https://habr.com/top/monthly/'
	print(get_data(get_html(url)))
main()