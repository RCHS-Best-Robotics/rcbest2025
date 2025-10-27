# Library imports
from vex import *

brain=Brain()
controller = Controller()
left_motor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
right_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True)
big_arm_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
small_arm_motor = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)

left_motor.spin(DirectionType.FORWARD)
right_motor.spin(DirectionType.FORWARD)
big_arm_motor.spin(DirectionType.FORWARD)
small_arm_motor.spin(DirectionType.FORWARD)

servoBL = Servo(brain.three_wire_port.a)
servoBR = Servo(brain.three_wire_port.c)
servoSL = Servo(brain.three_wire_port.e)
servoSR = Servo(brain.three_wire_port.g)

def big_arm_grab():
    servoBL.set_position(-43, DEGREES)
    servoBR.set_position(12, DEGREES)

def big_arm_release():
    servoBL.set_position(20, DEGREES)
    servoBR.set_position(-50, DEGREES)

def small_arm_grab():
    servoSL.set_position(-20, DEGREES)
    servoSR.set_position(20, DEGREES)    

def small_arm_release():
    servoSL.set_position(90, DEGREES)
    servoSR.set_position(-90, DEGREES)

def default_pos():
    servoBL.set_position(20, DEGREES)
    servoBR.set_position(-50, DEGREES)
    servoSL.set_position(90, DEGREES)
    servoSR.set_position(-90, DEGREES)
    
def comp_pos():
    servoBL.set_position(-43, DEGREES)
    servoBR.set_position(12, DEGREES)
    servoSL.set_position(-20, DEGREES)
    servoSR.set_position(20, DEGREES)    


test = False
run = True

default_pos()

while run == True:
    pos1 = int(controller.axis1.position())
    pos2 = int(controller.axis2.position())
    pos3 = int(controller.axis3.position())
    pos4 = int(controller.axis4.position())
    VfwdR = 0
    VfwdL = 0



    if(abs(pos4)<20):
        if(pos3>20):
            VfwdR = 100
            VfwdL = 100
        if(pos3<-20):
            VfwdR = -100
            VfwdL = -100
    elif(abs(pos3)<20):
        if(pos4>20):
            VfwdR = -100
            VfwdL = 100
        if(pos4<-20):
            VfwdR = 100
            VfwdL = -100

    else:
        VfwdR = pos3*(2/3) -pos4*(1/3)
        VfwdL = pos3*(2/3) +pos4*(2/3)
    
    
    

    print("pos4",pos4)
    print("pos3",pos3)
    left_motor.set_velocity((VfwdL), PERCENT)
    right_motor.set_velocity(-(VfwdR), PERCENT)

    if(abs(pos1)<20):
        big_arm_motor.set_velocity(pos2,PERCENT)
    


    if(controller.buttonR1.pressing()):
        big_arm_grab()
    
    if(controller.buttonR2.pressing()):
        big_arm_release()
    
    if(controller.buttonL1.pressing()):
        small_arm_grab()
    
    if(controller.buttonL2.pressing()):
        small_arm_release()


    if(controller.buttonA.pressing()):
        default_pos()

    if(controller.buttonB.pressing()):
        comp_pos()

    left_motor.spin(DirectionType.FORWARD)
    right_motor.spin(DirectionType.FORWARD)
    big_arm_motor.spin(DirectionType.FORWARD)
    small_arm_motor.spin(DirectionType.FORWARD)



while test == True:
    pos1 = controller.axis1.position()
    pos2 = controller.axis2.position()
    pos3 = controller.axis3.position()
    pos4 = controller.axis4.position()
    wait(2000, MSEC)
    brain.screen.clear_row(1)
    brain.screen.set_cursor(1,1)
    wait(20, MSEC)