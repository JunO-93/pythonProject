#내장 모듈

from math import pi, ceil as c
print(pi)
print(c((2.7)))


#외부 모듈
import pyautogui as pg #매크로


pg.moveTo(500, 500, duration=2)

pg.write("Hello world!", interval=0.1)

