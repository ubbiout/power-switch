# power-switch
hold to safely shut down your pi

I started from https://scribles.net/adding-power-switch-on-raspberry-pi/

but I don't want to reboot if the button is pressed accidentally

The idea is that it won't do anything unless you hold the button for a while, like 4 seconds.

ideally, use as litle system resources while waiting for a hold.

I'm not even sure starting a thread helps at all.
There is probably a better way to do it with just GPIO event interrupt calls.... maybe version 2

physical configuration:
https://pinout.xyz/pinout/pin5_gpio3
button pulling pin 5 low.
You won't be able to use I2C as pin 5 is I2C clock and I am using it to trigger the shutdown. 
You could instead use a second button to trigger shutdown... but pin 5 will wake the pi if the pi is off and you pull it to ground.
In my application, this code runs after reading the I2C Real Time Clock.
