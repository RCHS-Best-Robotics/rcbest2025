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
left_motor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True)
big_arm_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
small_arm_motor = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)

left_motor.spin(DirectionType.FORWARD)
right_motor.spin(DirectionType.FORWARD)
big_arm_motor.spin(DirectionType.FORWARD)
small_arm_motor.spin(DirectionType.FORWARD)

def bigarmup():
    big_arm_motor.set_velocity(50, PERCENT)

def bigarmdown():
    big_arm_motor.set_velocity(-50, PERCENT)

def smallarmclockwise():
    small_arm_motor.set_velocity(-50, PERCENT)

def smallarmcounterclockwise():
    small_arm_motor.set_velocity(50, PERCENT)

test = False
run = True

while run == True:
    pos1 = int(controller.axis1.position())
    pos2 = int(controller.axis2.position())
    pos3 = int(controller.axis3.position())
    pos4 = int(controller.axis4.position())
    VfwdL = pos3
    VfwdR = -pos3

    if pos4!=0:
        VfwdR = pos3 + pos4
        VfwdL = pos3 + pos4


    
    left_motor.set_velocity(VfwdL, PERCENT)
    right_motor.set_velocity(VfwdR, PERCENT)

    controller.buttonX.pressed(bigarmup)
    controller.buttonX.pressed(bigarmdown)
    controller.buttonX.pressed(smallarmclockwise)
    controller.buttonX.pressed(smallarmcounterclockwise)

    brain.screen.print("1: ",pos1,"; 2: ",pos2)
    brain.screen.print("; 4: ",pos4,"; 3: ",pos3)
    brain.screen.clear_row(1)
    brain.screen.set_cursor(1,1)
    



while test == True:
    pos1 = controller.axis1.position()
    pos2 = controller.axis2.position()
    pos3 = controller.axis3.position()
    pos4 = controller.axis4.position()
    brain.screen.print("1: ",pos1,"; 2: ",pos2)
    brain.screen.print("; 4: ",pos4,"; 3: ",pos3)
    wait(2000, MSEC)
    brain.screen.clear_row(1)
    brain.screen.set_cursor(1,1)
    wait(20, MSEC)