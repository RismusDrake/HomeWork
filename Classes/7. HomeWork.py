'''Седьмое задание. Получить курс нескольких валют за текущую дату.
 Сообщение в виде списка, вроде: «За 11.04.2019 курс 2.12 рублей за 1 Евро, 228… за 1 доллар». 
http://www.nbrb.by/APIHelp/ExRates'''



import requests															#Импорт библиотеки requests
from bs4 import BeautifulSoup											#Взятие отдельного элемента из библиотеки requests

def get_html(url):														#Создание функции get_html
	r = requests.get(url)
	return r.text

def get_data(html):														#Создание функции get_data
	soup = BeautifulSoup(html, 'lxml')
	Currency = soup.find('body').text
	return Currency

def main():																#Создание функции main и вывод результата
	url = 'http://www.nbrb.by/api/exrates/rates?periodicity=0'
	print(get_data(get_html(url)))
main()