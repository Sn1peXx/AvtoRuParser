from bs4 import BeautifulSoup
import requests
import os


def save():
	with open('D:\\python\\parser\\AvtoRU.txt', 'a', encoding='utf-8') as file:
		file.write(f'Машина {car["title"]} -> Инфо {car["info"]} -> Ссылка {car["link"]}\n\n')


def delFile():
	chek_file = os.path.exists('D:\\python\\parser\\AvtoRU.txt')
	if chek_file:
		path = 'D:\\python\\parser\\AvtoRU.txt'
		os.remove(path)
	else:
		pass

def parser():
	max_page = 17
	count = 0

	delFile()

	print('Введи марку интересущий вас машины (на англ. яз.)\nК примеру audi, nissan, kia')
	avto = input('Ввод: ')
		

	for x in range(1, max_page):
		URL = 'https://auto.ru/sankt-peterburg/cars/' + str(avto.lower()) + '/all/?page=2&output_type=list&page=' + str(x)

	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
	}

	#Отправляем запрос на страницу
	response = requests.get(URL, headers = HEADERS)
	# Получаем контент со страницы
	soup = BeautifulSoup(response.content, 'html.parser')
	#Получаем блок для парсинга
	items = soup.findAll('div', class_ = 'ListingItem-module__main')
	#Создаем пустой список
	cars = []

	for item in items:
		cars.append({
			'title': item.find('h3', class_ = 'ListingItemTitle-module__container ListingItem-module__title').get_text(strip = True),
			'info': item.find('div', class_ = 'ListingItemTechSummaryDesktop__cell' ).get_text(strip = True),
			'link': item.find('a', class_ = 'Link ListingItemTitle-module__link').get('href')
			})

		global car
		for car in cars:
			count += 1
			print(f'Машина {car["title"]} -> Инфо {car["info"]} -> Ссылка {car["link"]}')
			save()

	print(f'Вcего машин = {count}')
parser()