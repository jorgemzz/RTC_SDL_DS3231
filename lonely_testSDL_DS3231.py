# -*- coding: utf-8 -*-
# @Author: Jorge Miranda
# @Date:   2021-02-23 15:15:58
# @Last Modified by:   Jorge Miranda
# @Last Modified time: 2021-02-23 15:54:56

import time
import SDL_DS3231

ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)

#ds3231.write_now()

print("----------------------")
print("Testing DS3231 library")
print("----------------------")

while True:
	print("")
	print("Board time: \t%s" % time.strftime("%Y-%m-%d %H:%M:%S"))
	print("Ds3231 time: \t%s" % ds3231.read_datetime())
	print("Ds3231 Temp: \t%d" % ds3231.getTemp())
	time.sleep(10)