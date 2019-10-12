import requests

def get_usd():
	url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
	respones = requests.get(url).json()
	price = respones[4]['Cur_OfficialRate']
	print(price)

get_usd()