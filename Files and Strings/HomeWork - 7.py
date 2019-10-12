'''Седьмое задание. Разбить строку по нескольким разделителям'''


import re

line = 'adsf fjdk tasdgwd sa$dsfx gsdf,aion,food'
result = re.split(r'[;,\s]', line)
print(result)
