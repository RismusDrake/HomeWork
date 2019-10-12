from bot import MoneyBot
from bot_config import token
#from log import logg_this
from bot import Bot

try:

	test_bot = MoneyBot(token)
	money = test_bot.get_money()
	answer = test_bot.get_message()
	recorder = test_bot.record_message_to_file()
	#logg_this(answer)
	chat_id = answer['chat_id']
	text = answer['text']

	last_message = Bot(token)
	message = last_message.get_updates()
	test = message['result'][-6]['message']['text']

	if text == '/course':
		test_bot.send_message(chat_id, money)

	'''if text == '/write':
		test_bot.record_message_to_file(answer)
		test_bot.send_message_to_file(chat_id, 'done')

	else:
		test_bot.send_message(chat_id, 'Echo:' + text)'''

	if text == 'что я писал 5 сообщений назад?':
		test_bot.send_message(chat_id, '5 сообщений назад ты писал(а): ' + test)

except NameError:
	print('Проблема с переменной')
except TypeError:
	print('Type ошибка')
except SyntaxError:
	print ('Syntax ошибка')
except KeyError:
	print ('KeyError ошибка')
except:
	print ('Поймано исключение ... какое-то в файле "main"')
finally:
	print('Конец поимки в файле "main"')