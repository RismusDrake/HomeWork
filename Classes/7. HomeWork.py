'''Седьмое задание. Получить курс нескольких валют за текущую дату.
 Сообщение в виде списка, вроде: «За 11.04.2019 курс 2.12 рублей за 1 Евро, 228… за 1 доллар». 
http://www.nbrb.by/APIHelp/ExRates'''



import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text


def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	Currency = {"Cur_ID":145,"Date":"2019-09-23T00:00:00","Cur_Abbreviation":"USD","Cur_Scale":1,"Cur_Name":"Доллар США","Cur_OfficialRate":2.0412}, {"Cur_ID":290,"Date":"2019-09-23T00:00:00","Cur_Abbreviation":"UAH","Cur_Scale":100,"Cur_Name":"Гривен","Cur_OfficialRate":8.3587}, {"Cur_ID":298,"Date":"2019-09-23T00:00:00","Cur_Abbreviation":"RUB","Cur_Scale":100,"Cur_Name":"Российских рублей","Cur_OfficialRate":3.1980}
	return Currency


def main():
	url = 'http://www.nbrb.by/API/ExRates/Rates'
	print(get_data(get_html(url)))
main()