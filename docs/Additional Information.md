---
title: Additional Information
layout: default
nav_order: 7
---

{% include Header.html %}

## Additional Information ##

The information on this page is not required for normal assembly and use of the timer.  It's only provided to help with potential problems you may encounter and to provide some insight if you would like to learn more about using CircuitPython on microcontrollers and how they function. To a limited extent, the Touch_and_Go program can be further customized to suit your particular requirements.

**CircuitPython**

CircuitPython is a user friendly programming language.  It is a subset of the official Python language suitable for use on microcontrollers.  Everything you need to know about CircuitPython can be found in an extensive <a href="https://learn.adafruit.com/welcome-to-circuitpython" target="_blank">tutorial</a> from Adafruit.

A useful tool for interacting with the actual timer program is dedicated a code editor.  Adafruit recommends downloading and installing a user friendly editor called Mu.  The guide to installing Mu can be found <a href="https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor" target="_blank">here</a>. The code editor allows you to open the timer program code for editing and customizing.  As soon as you save your new code to the `CIRCUITPY` drive it will automatically start to run.  Unlike Arduino no pre-compiling is necessary.

The most useful feature of a code editor is the ability to connect and interact with a microcontroller using a serial console.  How to open a serial console window in Mu is described <a href="https://learn.adafruit.com/welcome-to-circuitpython/kattni-connecting-to-the-serial-console" target="_blank">here</a>.

Another feature of the serial console is called the REPL.  Using the REPL you can communicate directly with the microcontroller.  Using the REPL is explained <a href="https://learn.adafruit.com/welcome-to-circuitpython/the-repl" target="_blank">here</a>.

If only a simple revision to the program code is desired, the **main.py** file can be opened and edited using a simple text editor like Notebook or TextEdit.  After you save your revision the timer will automatically restart and run the revised code.

If you make an error in programming the **main.py** file can always be overwritten with a new downloaded copy.

**Trinket M0**

The Trinket M0 is a compact microcontroller development board that uses a ATSAMD21 microcontroller from Microchip Technologies.

The Trinket M0 it has a very limited memory capacity. It is possible to run into conditions were you may receive a warning that you have run out of space when trying to upgrade your program code.  If you encounter this issue try erasing the 'CIRCUITPY' drive using the REPL by following these <a href="https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting#to-erase-circuitpy-storage-dot-erase-filesystem-2987288" target="_blank">steps</a>. Once the drive has been erased then you should be able drag and drop the **main.py** file and the complete **lib** folder back onto the drive.

The Trinket M0 is fully operational when powered by either the ESC or the USB port.  As a matter of fact, there is built in diode protection and it can be safely powered by both simultaneously.

**Down the Rabbit Hole**

If you wish to learn more about electronics, both <a href="https://www.adafruit.com/" target="_blank">Adafruit</a> and <a href="https://www.sparkfun.com/" target="_blank">Sparkfun</a> can provide the supplies and equipment for experimenting and learning.   On the surface, both of these companies appear to be retailers of electronic devices for the maker community.  In reality, they are best described as companies with a primary goal of education.  To that end, they encourage experimentation by offering beginner orientated electronic products along with comprehensive online learning tutorials.



[1]: https://www.adafruit.com/
[2]: https://www.sparkfun.com/
