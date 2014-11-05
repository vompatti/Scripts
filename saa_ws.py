#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import string
import re
import time, sys

# Sää

locale="Helsinki"

url="http://ilmatieteenlaitos.fi/saa/Helsinki?parameter=4&map=weathernow&station=2978"

source=urllib.urlopen(url).read()

try:
	temp=re.findall("(-*\d+[,|\.]\d+)&nbsp;&deg;", source)
	windspeed=re.findall("(-*\d+[,|\.]*\d*)&nbsp;m\/s", source)
except IndexError:
	weather="0 0 0 0 0 0 0 0 0 0"

temp=float(string.replace(temp[0], ",", "."))
windspeed=float(string.replace(windspeed[0], ",", "."))

if (temp<2 and windspeed>2):
	wci=round(13.12+0.6215*temp-11.37*(3.6*windspeed)**0.16+0.3965*temp*(3.6*windspeed)**0.16, 1)
else:
	wci="-"

#print "%s (%s) °C" % (temp, wci)
print "%s m/s" % (windspeed)
