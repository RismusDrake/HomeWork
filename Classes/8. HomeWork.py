'''Восьмое задание. Получить список статей хабра за месяц.
https://habr.com/top/monthly/'''



import requests
from bs4 import BeautifulSoup

def get_html(url):
	r = requests.get(url)
	return r.text

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	h1 = soup.find('body').find('div', {'class' :"layout"}).find('div', {'class' :"layout__row layout__row_body"}).find('div', {'class' :"layout__cell layout__cell_body"}).find('section', {'class': "column-wrapper column-wrapper_lists js-sticky-wrapper"}).find('div', {'class':"posts_list"}).text
	return h1

def main():
	url = 'https://habr.com/top/monthly/'
	print(get_data(get_html(url)))
main()