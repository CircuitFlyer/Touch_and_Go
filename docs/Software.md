---
title: Software
layout: default
nav_order: 3
---

{% include Header.html %}

## Software Installation ##

One of the great features of the Touch_and_Go timer is the ability to update the program code as new features and improvements become available.

The instructions below cover two separate procedures.  The first procedure is used to install the program code onto a new microcontroller board.  The second procedure describes how to update your existing Touch_and_Go timers to the latest version.

{: .highlight}
Be sure to check here from time to time to make sure you are using the most up to date version of the program code.  **Latest Version: v1.4**

First, a bit of background on how CircuitPython functions: Whenever the timer is powered up, CircuitPython looks for a file called **main.py**, loads it into the memory and automatically begins to run the program.  The file name must be **main.py**.  Do not rename the file or use any other file name for the program code.  This may cause confusion when performing an update as both the previous version and the newest version will have the same file name.  Hence the requirement to always **overwrite and replace** the old version with the new version, do **not** keep both.

{: .highlight }
A quick note about micro-USB cables: If you have trouble getting the disk drive to show up on your computer there is a possibility you are not using a data cable.  There may be some USB cables that are used for charging only and are not data transfer cables.  Be sure you have the right one.

<span class="fs-6">
[Click Here to download the latest program code .zip file](https://github.com/CircuitFlyer/Touch_and_Go/archive/v1.4.zip){: .btn .btn-blue }
</span>

### Software Installation on a New Microcontroller: ###

**Step 1** - Download the .zip file from the link above.  Unzip the download and have a look inside.  You may see several different items listed there.  You are only interested in the file named **main** that has a file extension of **.py** (the python programming language file type) and a file named **adafruit-circuitpython-trinket_m0-en_US-4.1.2.uf2**.

**Step 2** - Connect the Trinket M0 to your computer using a micro-USB type cable.  The Trinket M0 will power up and a new removable drive called `CIRCUITPY` will appear on your computer.

**Step 3** - Quickly press the tiny reset button on the board **two** times.  The `CIRCUITPY` drive will disappear and a new drive called `TRINKETBOOT` will pop up.  Drag and drop the **adafruit-circuitpython-trinket_m0-en_US-4.1.2.uf2** file from the download to the `TRINKETBOOT` drive.  When it is finished saving the `TRINKETBOOT` drive will disappear and the `CIRCUITPY` drive will reappear.

**Step 4** - Open the `CIRCUITPY` drive to view the files inside. If you see three files named **.fseventsd**, **.metadata_never_index** and **.Trashes** ignore them (these files may be hidden on MacOS but may be visible on Windows computers). **Delete all other files on the drive**.

**Step 5** - Drag and drop the **main.py** file and the complete **lib** folder from the latest download onto the `CIRCUITPY` drive. The timer will restart and automatically begin running the new code.  

That’s it, congratulations, you’re all done. The DotStar LED should light-up a bright green indicating your new Touch_and_Go timer is ready to use.

**Step 6** - Eject the `CIRCUITPY` drive and unplug the USB cable from the timer.
<br>

### Update Your Existing Touch_and_Go Timer to the Latest Version: ###

If there is a newer release of the program code, use the following procedure to overwrite and replace only the one file called **main.py** on your timer.

**Step 1** - Download the .zip file from the link above.  Unzip the download and have a look inside.  You will see several different items listed there.  We are only going to use the file named **main.py**

**Step 2** - There is one very important requirement when upgrading from a previous version to v1.4: **Touch and hold the touch sensor pin when connecting the micro-USB cable**.  Hold it for at least 5 seconds then release.  This will remount the drive to allow access from the USB port.  Otherwise, you will not be able to make any changes. Thankfully, v1.4 will eliminate this requirement going forward.

A removable drive called `CIRCUITPY` will appear on your computer.

**Step 3** - Open the `CIRCUITPY` drive to view the files inside. If you see three files named **.fseventsd**, **.metadata_never_index** and **.Trashes** ignore them (these files may be hidden on MacOS but may be visible on Windows computers). **Delete all other files on the drive**.

**Step 4** - Next, drag and drop the **main.py** file and the complete **lib** folder from the latest download onto the `CIRCUITPY` drive.

Congratulations, you should now have an up-to-date Touch_and_Go timer.  The LED on the Trinket M0 should illuminate green to indicate that it's currently in Standby mode.  **Note**: the timer will be reset to the default values and will need reprogramming before your next flight.

**Step 5** - Eject the `CIRCUITPY` drive and unplug the USB cable from the timer
