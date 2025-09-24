# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       aiden                                                        #
# 	Created:      9/20/2025, 12:57:51 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()
controller = Controller()

while True:
    posx2 = controller.axis1.position()
    posy2 = controller.axis2.position()
    posy1 = controller.axis3.position()
    posx1 = controller.axis4.position()
    brain.screen.print("x2: ",posx2,"; y2: ",posy2)
    brain.screen.print("; x1: ",posx1,"; y1: ",posy1)
    wait(2000, MSEC)
    brain.screen.clear_row(1)
    brain.screen.set_cursor(1,1)
    wait(20, MSEC)



        
