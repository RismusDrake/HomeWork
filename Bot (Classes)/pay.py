import requests

money_url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'

def get_money():
	respone = requests.get(money_url).json()
	usd_price = eur_price = pln_price = 'NOT_FOUND' 
	for p in list(respone):
		if p['Cur_Abbreviation'] == 'USD':
			usd_price = p['Cur_OfficialRate']
		if p['Cur_Abbreviation'] == 'EUR':
			eur_price = p['Cur_OfficialRate']
		if p['Cur_Abbreviation'] == 'PLN':
			pln_price = p['Cur_OfficialRate']
	return f'Cost of one BYN today - {usd_price} USD, {eur_price} EUR, {pln_price} PLN'

print(get_money())
