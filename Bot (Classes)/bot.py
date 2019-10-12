import requests
from bot_config import token
from bot_config import time
#from log import logg_this

class Bot:

	try:

		def __init__(self, token):
			self.token = token
			self.url = f'https://api.telegram.org/bot{self.token}/'

		def get_updates(self):
			method = 'getUpdates'
			req = requests.get(self.url + method)
			return req.json()

		def get_message(self):
			data = self.get_updates()
			last_message = data['result'][-1]['message']
			chat_id = last_message['chat']['id']
			text = last_message['text']

			message = {'chat_id': chat_id,
					   'text': text}
			return message

		def send_message(self, chat_id, text):
			method = 'sendMessage'
			params = {'chat_id': chat_id,
					  'text': text}
			respone = requests.post(self.url + method, params)
			return respone

	except NameError:
		print('Name ошибка')
	except TypeError:
		print('Type ошибка')
	except ValueError:
		print('Value ошибка')
	except SyntaxError:
		print ('Syntax ошибка')
	except:
		print('Поймано исключение в классе "Bot"')
	finally:
		print('Конец поимки в классе "Bot"')

class MoneyBot(Bot):

	try:

		def __init__(self, token):
			super().__init__(token)
			self.money_url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'

		def get_money(self):
			respone = requests.get(self.money_url).json()
			usd_price = eur_price = pln_price = 'NOT_FOUND' 
			for p in list(respone):
				if p['Cur_Abbreviation'] == 'USD':
					usd_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'EUR':
					eur_price = p['Cur_OfficialRate']
				if p['Cur_Abbreviation'] == 'PLN':
					pln_price = p['Cur_OfficialRate']
			return f'Cost of one BYN today - {usd_price} USD, {eur_price} EUR, {pln_price} PLN'

		def record_message_to_file(self):
			with open('E:/Документы/Учёба/Программирование по Python/Занятия/lesson - 9/message.txt', 'w') as message_file:
				last_user_message = self.get_updates()['result'][-2]['message']['text']
				message_file.write(last_user_message + '\n')

	except NameError:
		print('Name ошибка')
	except TypeError:
		print('Type ошибка')
	except ValueError:
		print('Value ошибка')
	except SyntaxError:
		print ('Syntax ошибка')
	except:
		print('Поймано исключение в классе "MoneyBot"')	
	finally:
		print('Конец поимки в классе "MoneyBot"')



'''Что не хочет работать
		def record_message_to_file(self):
				with open('messages/message:' + ''.join(str(time).split(' ')) + '.txt', 'w') as message_file:
					last_user_message = self.get_updates()['result'][-2]['message']['text']
					message_file.write(last_user_message + '\n')

'''
