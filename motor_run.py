#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import nxt.locator
from nxt.motor import *

screen = curses.initscr()

#curses.noecho()
#curses.curs_set(0)
screen.keypad(1)
#screen.nodelay(1)

b = nxt.locator.find_one_brick()

m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)
vehicle = SynchronizedMotors(m_left, m_right, 0)

is_running = False

while True:
   key = screen.getch()
   if key == ord("q"): break
   elif key == curses.KEY_UP and is_running == False:
      vehicle.run()
      is_running = True
      
   elif key == curses.KEY_UP and is_running == True:
      vehicle.idle()
      is_running = False
   
curses.endwin()    
