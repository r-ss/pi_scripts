#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess

import xml.etree.ElementTree as etree
from urllib2 import urlopen

import datetime


def say(text):
	FNULL = open(os.devnull, 'w')
	subprocess.Popen(['mplayer', 'http://translate.google.com/translate_tts?tl=ru&ie=UTF-8&q=%s' % text], stdout=FNULL, stderr=subprocess.STDOUT) # call subprocess

def play(file):
	FNULL = open(os.devnull, 'w')
	subprocess.Popen(['mpg321', '/home/pi/misc/sounds/%s' % file], stdout=FNULL, stderr=subprocess.STDOUT) # call subprocess

#play('ding.mp3')
#say('Привет')



def say_weather(part):
	print 'get weather'
	city_id = 27347 #Ivanovo, Russia
	weather_url = "https://export.yandex.ru/weather-ng/forecasts/%d.xml" % city_id
	ns = lambda tag: "{http://weather.yandex.ru/forecast}" + tag # add namespace
	# download & parse xml with weather forecast
	root = etree.parse(urlopen(weather_url)).getroot()	 
	# find current weather
	temperature_now = root.find(ns('fact')).findtext(ns('temperature'))
	weather_type = root.find(ns('fact')).findtext(ns('weather_type'))
	day_sunrise = root.find(ns('day')).findtext(ns('sunrise'))
	day_sunset = root.find(ns('day')).findtext(ns('sunset'))
	if part == 'now':
		speech_string = u'Температура сейчас %s, %s' % (temperature_now, weather_type)
		speech_string += u'. Восход: %s, Закат: %s' % (day_sunrise, day_sunset)

	nodes = root.find(ns('day')).findall(ns('day_part'))
	for node in nodes:
		if node.attrib['type'] == 'day':
			temperature_day = nodes[2].find(ns('temperature-data')).findtext(ns('avg'))
			weather_type = node.findtext(ns('weather_type'))
			if part == 'day':
				speech_string = u'Температура днем %s, %s' % (temperature_day, weather_type)
		if node.attrib['type'] == 'evening':
			temperature_evening = nodes[2].find(ns('temperature-data')).findtext(ns('avg'))
			weather_type = node.findtext(ns('weather_type'))
			if part == 'evening':
				speech_string = u'Температура вечером %s, %s' % (temperature_evening, weather_type)
	say(speech_string)


def check_time():
	time = datetime.datetime.now()
	t = time.strftime('%H%M')


	if t == '0900':
		say_weather('now')
	if t == '0901':
		say_weather('day')
	if t == '0902':
		say_weather('evening')

	if t == '1000':
		say(u'Сейчас 10 часов. Собаку покорми')

	if t == '1100':
		play('nahil.mp3')

	if t == '1200':
		say(u'Сейчас 12 часов, например')

	if t == '1300':
		play('internetcity.mp3')

	if t == '1400':
		say(u'Сейчас 14 часов, например')

	if t == '1600':
		say(u'Сейчас 16 часов, например')

	if t == '2200':
		say(u'Сейчас 10 часов. Собаку покорми')


if __name__ == '__main__':
	#say_weather('evening')
	#play('ding.mp3')

	#say(u'Привет')

	check_time()
	print 'ok'
























