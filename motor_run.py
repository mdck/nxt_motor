
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import curses
import nxt.locator
from nxt.motor import *

screen = curses.initscr()

#curses.noecho() 
#curses.curs_set(0) 
screen.keypad(1) 

b = nxt.locator.find_one_brick()

m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)
vehicle = SynchronizedMotors(m_left, m_right, 0)

running = False
UP_key = False

while True: 
   key = screen.getch() 
   if key == ord("q"): break 
   elif key == curses.KEY_UP and running == False and UP_key == False: 
      vehicle.run() 
      running = True
      UP_key = True
   elif key == curses.KEY_UP and running == True and UP_key == True: 
      vehicle.idle()
      running = False
      UP_key = False

