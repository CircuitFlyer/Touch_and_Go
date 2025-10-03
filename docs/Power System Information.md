---
title: Power System Information
layout: default
nav_order: 6
---

{% include Header.html %}

## ESC Information ##

The details of how to program your ESC (Electronic Speed Controller) is outside the scope of these instructions.  Please refer to your ESC instruction manual for information.  If you are completely new to how electric control line power systems work, a brief overview can be found [here][1].

The timer should be compatible with the vast majority of ESCs available.  It will not work with ESCs that require a full throttle signal in order to arm the system before flight.

{: .warning }
IMPORTANT NOTE! The simplistic nature of the Touch_and_Go timer does **not** provide any protection to the ESC from overcurrent conditions. A stalled propeller, i.e. a nose-over or crash, can cause damaging high current flow in both the ESC and the motor windings. Use extra caution when flying off of grass circles.

As a reference guide, use the following table for suggested settings for ESC programming.

{: .highlight }
Note: The features described may or may *not* be present in the ESC you are using.

| ESC Programmable Feature | Recommended Setting |
| --- | :---: |
| RPM Governing | OFF |
| Brake setting | ON |
| Soft start | OFF |
| BEC Voltage Output | 5.0V or 5.5V Maximum |

## Throttle Calibration ##

The timer output signal covers a very wide throttle range and ESC throttle calibration is not usually required.  If you would like to calibrate your ESC throttle range, follow your ESC instructions and the following procedure:

**Step 1** - **Remove the propeller from the motor.**<br>
**Step 2** - Hold the timer touch pin while connecting the battery power.  The timer will start up and output a maximum throttle signal.<br>
**Step 3** - After the ESC is calibrated, release the timer touch pin.  The timer output will return to minimum throttle and the ESC should arm.<br>
**Step 4** - Disconnect the battery and re-install the propeller.



[1]: https://circuitflyer.com/electric%20power%20system%20101.html
