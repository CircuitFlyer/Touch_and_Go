#    ******************** 
#    *   Touch_and_Go   *
#    ********************

#  An Open Source Electric Control Line Timer by CircuitFlyer (a.k.a. Paul Emmerson).  A CircuitPython program for an
#  Adafruit microcontroller development board to create a timed PWM servo signal suitable to control a typical flight of an 
#  electric powered control line model aircraft.

# Board: Adafruit Trinket M0, https://www.adafruit.com/product/3500
# Firmware: CircuitPython 4.1.x 
# Timer Program Version: 1.2, www.circuitflyer.com, https://github.com/CircuitFlyer/Touch_and_Go

# Import required libraries and modules:

import board
import time
import os
import touchio
import pulseio
import adafruit_dotstar
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

# Set some things up to get started:

# Built in Dotstar LED
dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=1.0)  # maximum brightness can be adjusted

# Built in red LED (pin D13)
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Capacitive touch sensor on pin D3
touch = touchio.TouchIn(board.D3)
while (touch.raw_value > 3000):  # if pin is touched: wait (finger on the pin at boot-up for USB access)
    time.sleep(0.1)
touch.deinit()  # as soon as pin is not touched de-initialize and
touch = touchio.TouchIn(board.D3)  # restart, otherwise the threshold value will be too high and touch.value won't work

# Servo signal output on pin D4
servo_pwm = pulseio.PWMOut(board.D4, frequency=50)
servo = servo.Servo(servo_pwm, min_pulse=950, max_pulse=2150)
servo.fraction = 0  # set idle throttle ASAP in case ESC is looking for a signal

# Create some helper functions:

def dot_update(color, flash_interval):  # used to control the color and flash rate of the built in dotstar LED
    global show
    global flash_time
    global flash_count
    if (flash_interval == 0):  # if a solid color is required, turn it on
        dot[0] = color
        show = True
    if ((flash_interval > 0) and (now >= flash_time + flash_interval)):  # if the led is to flash, check to see if it's time to turn on or off
        if (show):  # if on, turn off
            dot[0] = BLANK
            show = False
        else:
            dot[0] = color  # if off, turn on
            if (long_touch):
                flash_count += 1  # record the number of flashes only if it's during a long touch (programming modes)
            show = True
        flash_time = now

def save_parameters():  # used to write any changed parameters to memory for the next flight
    parameters = [delay_time, flight_time, rpm]  # make the newest parameters into a list
    try:
        with open("parameters.bin", "wb") as file:  # open the file for writing (this will erase previous data)
            array = bytearray(parameters)
            file.write(array)  # write the new parameters as bytes
            file.close()
            print("Saved ", parameters)
    except OSError:
        print('Oops, write access from code not available, parameters not saved')  # if there is a problem

def program_select():  # used to select the various choices within the programming modes
    global mode
    global main_count
    if (main_count == 1):  # 1 touch - program the delay time
        mode = "program_delay"
        print(mode)
    if (main_count == 2):  # 2 touches  - program the flight time
        mode = "program_flight"
        print(mode)
    if (main_count == 3):  # 3 touches - program the RPM
        mode = "program_rpm"
        print(mode)
    if (main_count == 4):  # 4 touches - exits the programming mode and returns to standby ready to fly
        mode = "standby"
        print(mode)
    main_count = 0
 
def rpm_ramp(increment):  # used to ramp up or down the rpm over a period of time
    global last_time
    if (now > last_time + 0.1):  # update a new rpm 10 times a second
        servo.fraction += increment
        last_time = now
 
# Define a bunch of variables:

previous_touch = False
counter = 0
touch_time = 0
long_touch = False
end_of_long_touch = False
RED = (255, 0, 0)
YELLOW = (200, 200, 0)
ORANGE = (180, 100, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 120)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (210, 0, 255)
MAGENTA = (255, 0, 100)
WHITE = (255, 255, 255)
BLANK = (0, 0, 0)
show = True
done = False
flash_time = 0
mode = "standby"
flash_count = 0
last_time = 0
volt_comp = 0  # voltage compensation see flight mode
delay_time = 30  # default delay time (seconds) (byte)
flight_time = 24  # default flight time (10 second intervals) (byte)
rpm = 60  # default rpm setting (0 - 100) (byte)
TO_period = 2  # period in seconds for RPM to increase from idle to flight RPM
land_period = 4  # period in seconds for RPM to decrease from flight RPM to off
rpm_fraction = (rpm / 100)  # servo.fraction uses data from 0.0 - 1.0, converts integer into fraction
parameters = [delay_time, flight_time, rpm]  # make default parameters into a list

# Read saved parameters from memory:

try:
    with open("parameters.bin", "xb") as file:  # if the file does not exsist, create it
        array = bytearray(parameters)
        file.write(array)  # write the default byte parameters
        file.close()
except OSError:
    with open("parameters.bin", "rb") as file:  # if the file did exsist, open it for reading
        parameters = list(file.read())  # read the saved byte data
        delay_time = parameters[0]  # assign the saved data for use as the new current parameters
        flight_time = parameters[1]
        rpm = parameters[2]
        rpm_fraction = (rpm / 100)
        file.close()

# Main Loop

while True:
    led.value = touch.value  # link built-in red LED to touch pin
    now = time.monotonic()  # update current time
    main_count = 0  # clear previous short touch count
    
# each time through the main loop, the following will test the touch pin for # of short touches or if a long touch has been entered
    
    if (touch.value and not previous_touch):  # at the start of any touch
        time.sleep(.02)  # add a bit of simple debounce, nothing time sensitive here
        if (touch.value and not previous_touch):  # check it again, if still touched proceed
            touch_time = now
            counter += 1
            previous_touch = True
    
    if (not touch.value and previous_touch):  # at the end of any touch
        previous_touch = False
        if (long_touch):  # except long touches, don't count long touches
            counter = 0
            long_touch = False
            end_of_long_touch = True  # set flag
    
    if (now - touch_time > 1 and counter > 0 and not touch.value and not long_touch):  # delay before updating short touch count
        main_count = counter  # indicator that short count is complete
        counter = 0
    
    if (now - touch_time > 3 and touch.value and previous_touch):  # after holding a touch for 3 seconds
        long_touch = True
    
# Timer program code
    
    if (mode == "standby"):  # entered at power-up, from programming modes or an aborted delay mode
        dot_update(GREEN, 0)
        if (long_touch):  # starts the timer for a typical flight
            mode = "delay"  # normal way to exit this mode
            last_time = now  # start the timer for the start delay
            print(mode)
        if (main_count == 5):  # 5 short touches - enter the programming mode
            mode = "program_delay"  # alternate way to exit this mode
            print(mode)

    if (mode == "program_delay"):  # entered from standby or any other program mode
        if (long_touch):
            dot_update(YELLOW, 0.4)
        else:
            dot_update(YELLOW, 0)
        if (end_of_long_touch):
            delay_time = flash_count  # count the number of flashes (1 flash = 1 second of delay) and
            save_parameters()  # save the new parameter
            end_of_long_touch = False  # reset flag
            flash_count = 0  # reset count
            print('Delay ', delay_time)
        program_select()  # number of touches will determine where to go next
    
    if (mode == "program_flight"):  # entered from any other program mode
        if (long_touch):
            dot_update(CYAN, 0.4)
        else:
            dot_update(CYAN, 0)
        if (end_of_long_touch):
            flight_time = flash_count  # count the number of flashes (1 flash = 10 seconds of flight) and
            save_parameters()  # save the new parameter
            end_of_long_touch = False  # reset flag
            flash_count = 0  # reset count
            print('Flight time ', flight_time)
        program_select()  # number of touches will determine where to go next
    
    if (mode == "program_rpm"):  # entered from any other program mode
        if (now - touch_time > 0.2 and touch.value):  # at the start of the next long touch
            dot_update(MAGENTA, 0.05)  # flash quickly to warn of impending motor stat-up
        else:
            dot_update(MAGENTA, 0)
        if (long_touch):
            mode = "set_rpm"  # exit to the rpm setting mode
            print(mode)
            increment = (abs(.25 - rpm_fraction))/(10)  # calculate the size of the rpm increment for soft start rpm_ramp
            last_time = now
            servo.fraction = 0.25  # start motor at minimum RPM
        program_select()  # number of short touches determine where to go next

    if (mode == "set_rpm"):  # mode to run motor at flight RPM and adjust as required
        dot_update(MAGENTA, 0.2)
        if (servo.fraction < rpm_fraction and not done):  # used to soft start the motor up to flight rpm
            rpm_ramp(increment)
        if (servo.fraction >= rpm_fraction and not done):
            servo.fraction = rpm_fraction
            done = True  # soft start only at the beginning then the single & double touches take over to control the RPM
        if (main_count == 1 and servo.fraction < 0.98):  # if a single touch and below 1.0 maximum
            servo.fraction += 0.01  # speed it up a little
            print(servo.fraction)
        if (main_count == 2 and servo.fraction > 0.02): # if a double touch and above 0.0 minimum
            servo.fraction -= 0.01  # slow it down a little
            print(servo.fraction)
        if (counter == 3):   # three touches to stop motor and write new settings to memory
            print(servo.fraction)
            rpm_fraction = servo.fraction
            rpm = int(rpm_fraction * 100)  # calculate the value for storage
            print('RPM is ', rpm)
            save_parameters()  # save the parameters
            servo.fraction = 0  # stop the motor
            end_of_long_touch = False  # reset flag
            done = False  # reset for the next time
            mode = "program_rpm"  # exit to the beginning of the program RPM mode
    
    if (mode == "delay"):  # mode to count down the time of the delayed start
        if (end_of_long_touch and touch.value):  # after the long touch used to enter this mode is over, any touch while in delay mode will abort and return to standby
            mode = "standby"
            end_of_long_touch = False  # reset flag
            print(mode)
        if (now - last_time + 5 > delay_time):  # 5 seconds of warning flash before starting motor
            dot_update(WHITE, 0.05)
        else:
            dot_update(BLUE, 0.5)
        if (now - last_time > delay_time):  # after the programmed delay start the motor for take-off
            mode = "take-off"
            increment = (abs(.25 - rpm_fraction))/(TO_period * 10)  # calculate the size of the rpm increment for rpm_ramp
            last_time = now
            servo.fraction = 0.25  # start motor at minimum RPM
            print(mode)
    
    if (mode == "take-off"):  # mode to slowly ramp up the RPM for a smooth take-off
        dot_update(RED, 1)
        if (touch.value):  # any touch will kill the motor and end the flight
            mode = "flight_complete"
            print(mode)
        if (servo.fraction < rpm_fraction):  # ramp up RPM from idle to flight RPM
            rpm_ramp(increment)
        if (servo.fraction >= rpm_fraction):  # once the motor reaches flight RPM
            servo.fraction = rpm_fraction
            mode = "flight"
            last_time = now
            volt_comp = now
            print(mode)
    
    if (mode == "flight"):  # mode to time the lenght of flight
        dot_update(RED, 1)
        if (touch.value):  # any touch will kill the motor and end the flight
            mode = "flight_complete"
            print(mode)
        if (flight_time > 17):  # voltage compensation kicks in at 3 minute flight times and above
            if (now - volt_comp) >(flight_time/2):  # voltage compensation starting at 5% of flight time
                servo.fraction += .005  # boost the rpm a tiny bit
                volt_comp += ((flight_time * 9.5) / 7)  # boost it again at equal intervals over the remaining 95%
                print(servo.fraction)
        if (now - last_time + 11 > (flight_time * 10)):  # flash the dotstar for 10 seconds before the motor stops
            dot_update(WHITE, 0.05)
        if (now - last_time +1 > (flight_time * 10)):  # time is up, prep for landing
            mode = "landing"
            increment = -(abs(.25 - rpm_fraction))/(land_period * 10)  # calculate the size of the rpm increment for rpm_ramp
            last_time = now
            print(mode)
    
    if (mode == "landing"):  # used to slowly decrease the RPM for a smooth landing
        dot_update(RED, 0.25)
        if (touch.value):  # any touch will kill the motor and end the flight
            mode = "flight_complete"
            print(mode)
        if (servo.fraction > 0.22):  # ramp down the RPM from flight RPM to idle
            rpm_ramp(increment)
        if (servo.fraction <= 0.22):
            servo.fraction = 0  # stop the motor
            mode = "flight_complete"
            last_time = now
            print(mode)
    
    if (mode == "flight_complete"):  # used to latch the program in an endless loop to conclude the flight and stop the motor
        servo.fraction = 0  # the latched off prevents restarting without having to disconnect the battery and start over
        dot_update(BLANK, 0)  # for the next flight (hopefully with another fully charged battery)
    
    