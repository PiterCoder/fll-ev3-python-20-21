#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent, follow_for_ms 
from ev3dev2.sensor.lego import ColorSensor 
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4 
from time import sleep
import os

#устанавливаем стандартный экран для вывода сообщений print()
os.system('setfont Lat15-TerminusBold14')

#создаем пару моторов по танковой схеме 
tank = MoveTank(OUTPUT_A, OUTPUT_B)


#определянм датчики света
color_left = ColorSensor(INPUT_1)
color_right= ColorSensor(INPUT_2)
color_stop = ColorSensor(INPUT_4)

#устанавливпем режимы для рулевый(левыц,праввй) яркость отраденного
color_left.mode='COL-REFLECT'
color_right.mode='COL-REFLECT'
#для остановочного датчика редим цветов
color_stop.mode='COL-COLOR'

#print(color_left.value(),color_right.value())


#эта функция заставояет робота проехать n съездов, со скоростью 40 по линии
def run(n, speed = 40, k = 0.1):
 i = 0 #счетчик съездов
 old_color = 0 #цвет поля на преведущем измерении(нужно для определения сьездов)
 while i < n: #пока не проезали вме съезды
  #считанм ошибку
  error = (100 - color_left.value()) - (100 - color_right.value()) 
  sc=color_stop.value() #считываем цыет с латчика остановки
  print(sc,old_color, i) #отладочный вывод

  if sc == 1 and old_color == 6: #если тнкущий цвет черный и проштый белый то
   i += 1 #увеличивпем счетчик съездов
   old_color = sc #обновлчем преведущий цвет
  #обновляем скорости моторов
  tank.on(SpeedPercent(speed-k*error), SpeedPercent(speed+k*error)) 
  sleep(0.01) #ждем
 #при выходе из цикла останавливанм моторы.
 tank.on(SpeedPercent(0), SpeedPercent(0))

run(3)
