---
title: Operation
layout: default
nav_order: 5
---

{% include Header.html %}

## Operating Instructions ##

Install the timer and connect to the ESC as discussed in the assembly instructions.

{: .warning }
SAFETY FIRST!  Any time the battery is connected stay clear of the prop.  The aircraft should always be held or secured until the pilot is ready.  When the flight ends the pilot should wait until their helper disconnects the battery before putting the handle down.

For a typical flight first connect the battery, after booting up the LED will turn green (Standby Mode) and the ESC should emit a signal to indicate it is armed and ready to start.  When ready, touch and hold the pin (a long touch of a minimum 3 seconds) to enter the Start Delay mode (flashing blue).  **Caution (NEW for v1.4)**: The motor will spin up briefly then stop. This indicates the start of the countdown timer before the motor starts to rotate.  During the last 5 seconds of the countdown the LED will change to white and flash quickly to warn of the impending startup of the motor.

{: .highlight }
Note: Any touch of the pin during the Start Delay mode will stop the countdown and return to the Standby mode (green).

After the Start Delay the Flight mode will start (flashing red) and the motor RPM will increase to the programmed flight RPM over a 2 second period.  This will assist with a smooth take-off.

{: .highlight }
After the motor starts **any touch of the pin will stop the motor** and jump to the Flight Complete mode (LED off).

To compensate for the decreasing battery voltage, any flight set for 3 minutes or longer will have periodic increases in the RPM signal to maintain a constant speed throughout of the flight.   10 seconds before the motor stops the LED will quickly flash white to indicate the end of the flight.  **(NEW for v1.4)** In addition to the flashing LED the motor RPM will briefly decrease and then resume normal RPM to help get the pilots attention. At the end of the flight the RPM will increase briefly before stopping to aid in a smooth approach and landing.  Once the motor stops the program enters the Flight Complete mode (LED off).  The power must be reset in order to exit the Flight Complete mode.

Disconnect the battery, replace it with a fully charged one and repeat the process for the next flight..
