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
left_motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
left_motor.set_velocity(100, PERCENT)
right_motor.set_velocity(100, PERCENT)
left_motor.spin(DirectionType.FORWARD)
right_motor.spin(DirectionType.FORWARD)
wait(2, SECONDS)
left_motor.stop()
right_motor.stop()
test = False
run = True

while run == True:
    posxR = controller.axis1.position()
    posyR = controller.axis2.position()
    posyL = controller.axis3.position()
    posxL = controller.axis4.position()
    VfwdL = posyL
    VfwdR = posyL
    
    if(posxL>0):
        VfwdL = VfwdL-abs(posxL)
    else:
        VfwdR = VfwdR-abs(posxL)
    left_motor.set_velocity(VfwdL, PERCENT)
    right_motor.set_velocity(VfwdR, PERCENT)

    if(posyL<0):
        left_motor.spin(DirectionType.REVERSE)
        right_motor.spin(DirectionType.REVERSE)
    else:
        left_motor.spin(DirectionType.FORWARD)
        right_motor.spin(DirectionType.FORWARD)
    



while test == True:
    posxR = controller.axis1.position()
    posyR = controller.axis2.position()
    posyL = controller.axis3.position()
    posxL = controller.axis4.position()
    brain.screen.print("xR: ",posxR,"; yR: ",posyR)
    brain.screen.print("; xL: ",posxL,"; yL: ",posyL)
    wait(2000, MSEC)
    brain.screen.clear_row(1)
    brain.screen.set_cursor(1,1)
    wait(20, MSEC)




        

def map_input(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min