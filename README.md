# networkJoy
Setup for running a gamepad across a network -- Made for relaying an N64 controller from a Raspberry Pi to a Windows host

I am using https://github.com/marqs85/gamecon_gpio_rpi/ for the N64 driver

How it works:
The linux server is just the event device piped into a network port. The Windows client reads the events off the network stream, keeps track of the controller state, and updates vJoy.

Prerequesites:
Requires numpy and vJoy
Use pip to get numpy
Get vJoy from http://vjoystick.sourceforge.net/site/index.php/download-a-install/download

To set up the Windows client:
Download this repo
Create one vJoy gamepad with X, Y, Rx, and Ry Axes, 10 buttons, no Force Feedback, and no POVs
Edit the networkJoy.py script to change the server and the port to your RPi

Run this on the Pi to start the Linux server:
cat /dev/input/js0 | nc -lkp 1964

Replace /dev/input/js0 with the path to your joystick events and replace 1964 with the port you want to use.
