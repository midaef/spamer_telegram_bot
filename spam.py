
import requests #импорт библиотеки requests
import random #импорт библиотеки random
import json #импорт библиотеки json
import threading #импорт библиотеки threading
import sys #импорт библиотеки sys

tokens = [''] #добавление токенов

chat_id = '@rfsdfgsdfgsdfg' #id чата
start_text = 'Are you ready to spam?)))' #текст начала спама
text = [] #тексты для спама
sendwhat = 'images' #выбор чем спамить
url = 'https://api.telegram.org/bot' #ссылка для спама
photo = [] #массив пикч


def send_message(token, chat_id, text): #метод отправки сообщения
	r = requests.get(url + token + '/sendmessage?' + 'chat_id=' + chat_id + '&text=' + text) #отправка сообщения


def send_photo(token, chat_id, photo): #метод отправки картинки
	r = requests.get(url + token + '/sendphoto?' + 'chat_id=' + chat_id + '&photo=' + photo) #отправа картинки


def spam(nn): #функция спама
	global nbots #добавление глобальной переменной в функцию
	global bfk #добавление глобальной переменной в функцию
	if sendwhat == 'text': #при отправке текста
		send_message(nn, chat_id, text[random.randrange(len(text))]) #отправка соощбения
	elif sendwhat == 'images': #при отправке картинки
		send_photo(nn, chat_id, photo[random.randrange(len(photo))]) #отправка картинки
			


def main(): #главная функция
	global nbots #добавление глобальной переменной в функцию
	global bfk #добавление глобальной переменной в функцию
	global photo #добавление глобальной переменной в функцию
	global text  #добавление глобальной переменной в функцию
	if sendwhat == 'images': #при отправке картинки
		f = open('img.txt', 'r') #открытие файла с url картинками
		for i in f: #цикл чтения файла
			s = i.lstrip() #удаление пробелов в начале строки
			s = s.rstrip() #удаление пробелов в конце строки
			photo.append(s) #добавление в массив с катинками
	if sendwhat == 'text': #при отправке текста
		f = open('text.txt', 'r') #открытие файла текстами
		for i in f: #цикл чтения файла
			s = i.lstrip() #удаление пробелов в начале строки
			s = s.rstrip() #удаление пробелов в конце строки
			text.append(s)	#добавление в массив с текстами	
	send_message(tokens[random.randrange(0, len(tokens))], chat_id, start_text) #отправка случайным ботов сообщения о готовности
	input('press to spam') #ожидание нажатия клавиши ENTER для запуска спама
	print('spam is starting') #вывод сообщения о начале спама
	nbots = len(tokens) #кол-во ботов
	while True: #бесконечный цикл
		t = [] #создание массива для потоков
		print('cycle started') #вывод сообщения о начале цикла
		for ii in tokens: #цикл инициализации потоков
			t.append(threading.Thread(target=spam(ii))) #инициализация потоков
		for ii in range(len(tokens)): #цикл старта потоков
			t[ii].start() #старт потоков
		for ii in range(len(tokens)): #цикл завершения потоков
			t[ii].join() #завершение потоков
		print('cycle stopped') #вывод сообщения о конце цикла

if __name__ == '__main__': #проверка запуска программы
	main() #запуск главной функции main()