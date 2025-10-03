---
title: Programming
layout: default
nav_order: 4
---

{% include Header.html %}

## Programming the Custom Settings ##

Using a simple procedure the Delay Time (the amount of time between initiating the timer sequence to when the motor starts-up), Flight Time (total motor run time) and RPM (speed of the motor) can be changed as follows:



Connect the ESC as discussed in the assembly instructions.  The capacitive touch pin is used for operator input.  This is similar to the touch sensitive screen on a smart-phone.  Hint: the more area of contact between your fingertip and the touch pin the better.  In other words, it works best with a positive gesture not a light touch.  

A **long touch** is a sustained touch for a minimum of 3 seconds.  A **tap or series of taps** is a single or multiple quick tap on the pin.  You will notice a 1 second delay after the last tap before the desired action takes place.  This short waiting period is needed to make sure all of the taps are complete.

{: .warning }
SAFETY FIRST!  Any time the battery is connected stay clear of the prop. For testing purposes, a good practice is to remove the prop from the motor.  Any energized aircraft should always be held or secured until the pilot is ready.

When you connect the battery to the ESC the board will boot-up and the DotStar LED will illuminate bright green (Standby Mode).  At this point the board will output an “idle” signal to the ESC.  The ESC should complete its initialization and arming sequence.  If the ESC does not complete the arming sequence, please refer to the FAQ section for some troubleshooting steps.

**Step 1** - 5 taps on the touch pin will enter the programming mode – the LED will change to yellow (Program Start Delay)

**Step 2** - To move between the three available programming modes:<br>

1 tap for Program Start Delay (yellow)<br>
2 taps for Program Flight Time (cyan)<br>
3 taps for Program RPM (magenta)<br>

**Step 3** - To change a setting while in the programming mode:

**Program Start Delay (yellow):**  Touch and hold the pin (long touch).  After a short delay the LED will flash.  Count the number of flashes.  Each flash = 1 second of delay.  Release the pin when you reach the desired count.

**Program Flight Time (cyan):**  Touch and hold the pin.  After a short delay the LED will flash.  Count the number of flashes.  Each flash = 10 seconds of flight time.  Release the pin when you reach the desired count.

**Program RPM (magenta):**

{: .warning }
You are about to run the motor at its flight RPM, secure the aircraft and stay clear of the prop.  The next thing to always remember: **3 TAPS TO STOP THE MOTOR**.

To start the motor, touch and hold the pin.  The LED will flash quickly to warn of the impending start-up.  After a short delay the motor will start and accelerate to the last programmed flight RPM.  Release the pin and the motor will stay running.

While the motor is running:<br>
1 tap on the pin will increase the RPM.<br>
2 taps will decrease the RPM.<br>  

Be sure to wait about a second between each set of taps for the RPM to change. Use a tachometer for a more precise setting of the RPM.  Avoid prolonged running on the ground as some electrical components may get hot.

When the desired RPM is reached:<br>
**3 TAPS TO STOP THE MOTOR.**<br>

**Step 4** - 4 taps to exit the programming mode and return to Standby (green).  Any new settings you enter will automatically be saved to memory and used for subsequent flights.
