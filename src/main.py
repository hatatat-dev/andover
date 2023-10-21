 # ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       kids                                                         #
# 	Created:      8/5/2023, 2:16:39 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")
#region VEXcode Generated Robot Configuration
from vex import *

# Brain should be defined by default
brain=Brain()

direction = True # counterclockwise (reverse in v5) :O
# Originally True, use not direction for False

# Robot configuration code
left_motor_a = Motor(Ports.PORT16, GearSetting.RATIO_6_1, direction)
left_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_6_1, direction)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT6, GearSetting.RATIO_6_1, not direction)
right_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_6_1, not direction)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 0.4444444444444444)
controller_1 = Controller(PRIMARY)
catapult_motor_a = Motor(Ports.PORT9, GearSetting.RATIO_18_1, not direction)
catapult_motor_b = Motor(Ports.PORT19, GearSetting.RATIO_18_1, direction)
catapult_motor_c = Motor(Ports.PORT18, GearSetting.RATIO_18_1, not direction)
catapult = MotorGroup(catapult_motor_a, catapult_motor_b, catapult_motor_c)
IntakeUpDown = Motor(Ports.PORT8, GearSetting.RATIO_18_1, not direction)
IntakeSpin = Motor(Ports.PORT7, GearSetting.RATIO_18_1, not direction)
bumper_stop = Distance(Ports.PORT7)
sideskirt = DigitalOut(brain.three_wire_port.g)
# sideskirtright = DigitalOut(brain.three_wire_port.d)
sideskirt.set(False)
# I didn't know what the ports were so fill in the port letter before running :)))))

#HELLO THIS IS EVA :) HAHAHAHAHAHAHAHAHAHhahahahhah
#DO NOR DELETE PLZ TYSM no🧢 BIG TRUST FR FR HAGS TRUST ME BRO GIT TRIPPIN' GIF IS PRONOUNCED GIF 
# I am an absolute RIZZLER im the RIZZARD of Oz 🧙‍♂️😬😎 I ate RIZZoto for lunch, you are what you eat. I HAVE IMMACULATE RIZZ 





# wait for rotation sensor to fully initialize
wait(30, MSEC)



def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")


# define variables used for controlling motors based on controller inputs
controller_1_left_shoulder_control_motors_stopped = True
controller_1_right_shoulder_control_motors_stopped = True
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False


# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, controller_1_left_shoulder_control_motors_stopped, controller_1_right_shoulder_control_motors_stopped, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:


            # DRIVETRAIN CODE
            

            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3
            # right = axis2
            drivetrain_left_side_speed = controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis2.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                if drivetrain_l_needs_to_be_stopped_controller_1: # check if motor has been stopped
                    left_drive_smart.stop()
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True

            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    right_drive_smart.stop()
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)

            # while controller_1.buttonC.pressing():
            #     catapult.stop()
            # if controller_1.buttonB.pressing():
            # while controller_1.buttonB.pressing():
            #     controller_1_buttonB()
                    
                    

            # INTAKE CODE


            # check the buttonL1/buttonL2 status
            # to control IntakeUpDown
            if controller_1.buttonL1.pressing():
                IntakeUpDown.spin(FORWARD)
                controller_1_left_shoulder_control_motors_stopped = False
            elif controller_1.buttonL2.pressing():
                IntakeUpDown.spin(REVERSE)
                controller_1_left_shoulder_control_motors_stopped = False
            elif not controller_1_left_shoulder_control_motors_stopped:
                IntakeUpDown.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_left_shoulder_control_motors_stopped = True
            # check the buttonR1/buttonR2 status
            # to control IntakeSpin
            if controller_1.buttonR1.pressing():
                IntakeSpin.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False

                # while bumper_a.pressing() == False:
                #     catapult.spin(FORWARD)
                
                # while bumper_a.pressing():
                #     catapult.stop()
                    
                # if controller_1.buttonA.pressing():
                #     catapult.spin(FORWARD)

            elif controller_1.buttonR2.pressing():
                IntakeSpin.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                IntakeSpin.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_right_shoulder_control_motors_stopped = True
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration
myVariable = 0

def sideskirt_extend():
    sideskirt.set(True)
def sideskirt_retract():
    sideskirt.set(False)
# when you want use the sideskirt you have to hold down the button so we can use those controller dohickeys to hook up to button left or we can remap later

def auton():
    drivetrain.set_drive_velocity(70, VelocityUnits.PERCENT)

    drivetrain.drive_for(REVERSE, 18, INCHES, wait=True)
    drivetrain.turn_for(RIGHT, 45, wait=True)
    drivetrain.drive_for(REVERSE, 13, wait=True)
    drivetrain.drive_for(FORWARD, 13, wait=True)
    drivetrain.turn_for(LEFT, 45, wait=True)
    drivetrain.drive_for(FORWARD, 9, wait=True)
    sideskirt.set(True)

    drivetrain.turn_for(LEFT, 45, wait=True)

    sideskirt.set(False)

    drivetrain.turn_for(LEFT, 45, wait=True)
    drivetrain.drive_for(FORWARD, 5, wait=True)
    drivetrain.turn_for(LEFT, 45, wait=True)
    drivetrain.drive_for(FORWARD, 37, wait=True)
    sideskirt.set(True) 

def when_started1():
    global myVariable
    auton()
    pass

def onevent_controller_1buttonA_pressed_0():
    global myVariable
    catapult.spin(FORWARD)
    while not not controller_1.buttonA.pressing():
        wait(5, MSEC)
    catapult.stop()

def onevent_controller_1buttonUp_pressed_0():
    global myVariable
    pass


def onevent_controller_1buttonL1_pressed_0():
    global myVariable
    pass

def onevent_controller_1buttonDown_pressed_0():
    global myVariable
    pass

def onevent_controller_1buttonL2_pressed_0():
    global myVariable
    pass

    catapult.stop()   
    # while controller_1.buttonB.pressing():
    #     catapult.spin(FORWARD)
    #     while bumper_a.pressing():
    #         print('bumper pressed!!!!')
    #         catapult.stop()
    #     # while catbutton == False:
    #     #     catapult_motor_a.spin()




# system event handlers
controller_1.buttonA.pressed(onevent_controller_1buttonA_pressed_0)
controller_1.buttonUp.pressed(onevent_controller_1buttonUp_pressed_0)
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonDown.pressed(onevent_controller_1buttonDown_pressed_0)
controller_1.buttonL2.pressed(onevent_controller_1buttonL2_pressed_0)
controller_1.buttonB.pressed(sideskirt_extend)
controller_1.buttonY.pressed(sideskirt_retract)
# add 15ms delay to make sure events are registered correctly.

def vexcode_auton_function():
    pass
    # auton_task_0 = Thread(auton)

wait(15, MSEC)

when_started1()

        