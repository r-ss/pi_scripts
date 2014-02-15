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


def get_weather():
	print 'get weather'
	city_id = 27347 #Ivanovo, Russia
	weather_url = "https://export.yandex.ru/weather-ng/forecasts/%d.xml" % city_id
	ns = lambda tag: "{http://weather.yandex.ru/forecast}" + tag # add namespace
	# download & parse xml with weather forecast
	root = etree.parse(urlopen(weather_url)).getroot()	 
	# find current weather
	temperature_now = root.find(ns('fact')).findtext(ns('temperature'))
	temperature_short = root.find(ns('fact')).findtext(ns('weather_type_short'))

	print u'Погода сейчас: %s, %s' % (temperature_now, temperature_short)





if __name__ == '__main__':
    get_weather()