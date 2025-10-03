#    ********************
#    *   Touch_and_Go   *
#    ********************
# Optimized Version 1.4 - Memory-efficient with NVM storage

import board
import time
import touchio
import pulseio
import adafruit_dotstar
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction
from microcontroller import nvm

# Mode constants (replaces string modes to save memory)
M_STANDBY, M_DELAY, M_TAKEOFF, M_FLIGHT, M_LANDING, M_COMPLETE = 0, 1, 2, 3, 4, 5
M_PROG_DELAY, M_PROG_FLIGHT, M_PROG_RPM, M_SET_RPM = 6, 7, 8, 9

# Color constants (only essential colors)
GREEN = (0, 255, 0)
YELLOW = (200, 200, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 100)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLANK = (0, 0, 0)

# Hardware setup
dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=1.0)
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Servo setup
servo_pwm = pulseio.PWMOut(board.D4, frequency=50)
servo = servo.Servo(servo_pwm, min_pulse=950, max_pulse=2050)
servo.fraction = 0

# Touch sensor setup
touch = touchio.TouchIn(board.D3)
if touch.raw_value > 3000:
    servo.fraction = 1
while touch.raw_value > 3000:
    time.sleep(0.1)
touch.deinit()
servo.fraction = 0
touch = touchio.TouchIn(board.D3)

# Functions
def dot_update(color, flash_interval):
    global show, flash_time, flash_count
    if flash_interval == 0:
        dot[0] = color
        show = True
        return
    if now >= flash_time + flash_interval:
        show = not show
        dot[0] = color if show else BLANK
        if long_touch:
            flash_count += 1
        flash_time = now

def save_parameters():
    nvm[0] = delay_time
    nvm[1] = flight_time
    nvm[2] = rpm

def load_parameters():
    global delay_time, flight_time, rpm, rpm_fraction
    # Check if NVM has been initialized (byte 0 will be 255 if never written)
    if nvm[0] == 255:
        # First time - write defaults
        save_parameters()
    else:
        # Load saved values
        delay_time = nvm[0]
        flight_time = nvm[1]
        rpm = nvm[2]
        rpm_fraction = rpm / 100

def program_select():
    global mode, main_count
    if main_count == 1:
        mode = M_PROG_DELAY
    elif main_count == 2:
        mode = M_PROG_FLIGHT
    elif main_count == 3:
        mode = M_PROG_RPM
    elif main_count == 4:
        mode = M_STANDBY
    main_count = 0

def rpm_ramp(increment):
    global last_time
    if now > last_time + 0.1:
        servo.fraction = max(min(servo.fraction + increment, rpm_fraction), 0) + .001
        last_time = now

# Variables
previous_touch = False
counter = 0
touch_time = 0
long_touch = False
end_of_long_touch = False
show = True
done = False
flash_time = 0
mode = M_STANDBY
flash_count = 0
last_time = 0
volt_comp = 0
main_count = 0
warning = False

# Default parameters
delay_time = 30
flight_time = 24
rpm = 60
rpm_fraction = rpm / 100

# User adjustable
TO_period = max(2, 1)
battery_boost = True

# Load saved parameters from NVM
load_parameters()

# Main Loop
while True:
    led.value = touch.value
    now = time.monotonic()
    main_count = 0

    # Touch detection with debounce
    if touch.value and not previous_touch:
        time.sleep(0.02)
        if touch.value:
            touch_time = now
            counter += 1
            previous_touch = True

    if not touch.value and previous_touch:
        time.sleep(0.02)
        if not touch.value:
            previous_touch = False
            if long_touch:
                counter = 0
                long_touch = False
                end_of_long_touch = True

    if now - touch_time > 1 and counter > 0 and not touch.value and not long_touch:
        main_count = counter
        counter = 0

    if now - touch_time > 3 and touch.value and previous_touch:
        long_touch = True

    # State machine
    if mode == M_STANDBY:
        dot_update(GREEN, 0)
        if long_touch:
            mode = M_DELAY
            servo.fraction = .20
            time.sleep(.5)
            servo.fraction = 0
            last_time = now
        if main_count == 5:
            mode = M_PROG_DELAY

    elif mode == M_PROG_DELAY:
        dot_update(YELLOW, 0.4 if long_touch else 0)
        if end_of_long_touch:
            delay_time = flash_count
            save_parameters()
            end_of_long_touch = False
            flash_count = 0
        program_select()

    elif mode == M_PROG_FLIGHT:
        dot_update(CYAN, 0.4 if long_touch else 0)
        if end_of_long_touch:
            flight_time = flash_count
            save_parameters()
            end_of_long_touch = False
            flash_count = 0
        program_select()

    elif mode == M_PROG_RPM:
        dot_update(MAGENTA, 0.05 if (now - touch_time > 0.2 and touch.value) else 0)
        if long_touch:
            mode = M_SET_RPM
            increment = abs(0.25 - rpm_fraction) / 10
            last_time = now
            servo.fraction = 0.15
        program_select()

    elif mode == M_SET_RPM:
        dot_update(MAGENTA, 0.2)
        if servo.fraction < rpm_fraction and not done:
            rpm_ramp(increment)
        if servo.fraction >= rpm_fraction and not done:
            servo.fraction = rpm_fraction
            done = True
        if main_count == 1 and servo.fraction < 0.98:
            servo.fraction += 0.01
        if main_count == 2 and servo.fraction > 0.02:
            servo.fraction -= 0.01
        if counter == 3:
            rpm_fraction = servo.fraction
            rpm = int(rpm_fraction * 100)
            save_parameters()
            servo.fraction = 0
            end_of_long_touch = False
            done = False
            mode = M_PROG_RPM

    elif mode == M_DELAY:
        if end_of_long_touch and touch.value:
            mode = M_STANDBY
            end_of_long_touch = False
        dot_update(WHITE if now - last_time + 5 > delay_time else BLUE, 0.05 if now - last_time + 5 > delay_time else 0.5)
        if now - last_time > delay_time:
            mode = M_TAKEOFF
            increment = abs(0.25 - rpm_fraction) / (TO_period * 10)
            last_time = now
            servo.fraction = 0.15

    elif mode == M_TAKEOFF:
        dot_update(RED, 1)
        if touch.value and (end_of_long_touch or not previous_touch):
            mode = M_COMPLETE
        if servo.fraction < rpm_fraction:
            rpm_ramp(increment)
        if servo.fraction >= rpm_fraction:
            servo.fraction = rpm_fraction
            mode = M_FLIGHT
            last_time = now
            volt_comp = now

    elif mode == M_FLIGHT:
        dot_update(WHITE if now - last_time + 11 > flight_time * 10 else RED, 0.05 if now - last_time + 11 > flight_time * 10 else 1)
        if touch.value and (end_of_long_touch or not previous_touch):
            mode = M_COMPLETE
        if flight_time > 17 and now - volt_comp > flight_time / 2:
            if battery_boost and servo.fraction < 0.99:
                servo.fraction += 0.005
            volt_comp += (flight_time * 9.5) / 7
        if now - last_time + 11 > flight_time * 10 and servo.fraction >= 0.2 and not warning:
            servo.fraction -= 0.1
            time.sleep(1.5)
            servo.fraction += 0.1
            warning = True
        if now - last_time + 1 > flight_time * 10:
            mode = M_LANDING
            last_time = now

    elif mode == M_LANDING:
        dot_update(RED, 0.25)
        if touch.value:
            mode = M_COMPLETE
        servo.fraction += min(0.1, (1 - servo.fraction))
        time.sleep(1.5)
        servo.fraction = 0
        mode = M_COMPLETE
        last_time = now

    elif mode == M_COMPLETE:
        servo.fraction = 0
        dot_update(BLANK, 0)
