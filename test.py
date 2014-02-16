#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess

import xml.etree.ElementTree as etree
from urllib2 import urlopen


def say(text):
	FNULL = open(os.devnull, 'w')
	subprocess.Popen(['mplayer', 'http://translate.google.com/translate_tts?tl=ru&ie=UTF-8&q=%s' % text], stdout=FNULL, stderr=subprocess.STDOUT) # call subprocess



#say('привет')

print u'привет'


def get_weather():
	print 'get weather'
	city_id = 27347 #Ivanovo, Russia
	weather_url = "https://export.yandex.ru/weather-ng/forecasts/%d.xml" % city_id
	ns = lambda tag: "{http://weather.yandex.ru/forecast}" + tag # add namespace
	# download & parse xml with weather forecast
	root = etree.parse(urlopen(weather_url)).getroot()	 
	# find current weather
	temperature_now = root.find(ns('fact')).findtext(ns('temperature'))
	weather_type = root.find(ns('fact')).findtext(ns('weather_type'))

	print u'Погода сейчас: %s, %s' % (temperature_now, weather_type)

	nodes = root.find(ns('day')).findall(ns('day_part'))
	if nodes[1].attrib['type'] == 'day':
		temperature_evening = nodes[2].find(ns('temperature-data')).findtext(ns('avg'))
		weather_type = nodes[2].findtext(ns('weather_type'))
		print u'Днем: %s, %s' % (temperature_evening, weather_type)
	if nodes[2].attrib['type'] == 'evening':
		temperature_evening = nodes[2].find(ns('temperature-data')).findtext(ns('avg'))
		weather_type = nodes[2].findtext(ns('weather_type'))
		print u'Вечером: %s, %s' % (temperature_evening, weather_type)


if __name__ == '__main__':
	get_weather()
	print 'ok'