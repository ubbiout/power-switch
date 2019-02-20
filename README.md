# power-switch
hold to safely shut down your pi

I started from https://scribles.net/adding-power-switch-on-raspberry-pi/ <br />
but I don't want to reboot if the button is pressed accidentally <br />
The idea is that it won't do anything unless you hold the button for a while, like 4 seconds.<br />
ideally, use as litle system resources while waiting for a hold.<br />

I'm not even sure starting a thread helps at all.<br />
There is probably a better way to do it with just GPIO event interrupt calls.... maybe version 2

physical configuration: <br />
https://pinout.xyz/pinout/pin5_gpio3 <br />
button pulling pin 5 low. <br />
You won't be able to use I2C as pin 5 is I2C clock and I am using it to trigger the shutdown.  <br />
You could instead use a second button to trigger shutdown... <br /> 
but pin 5 will wake the pi if the pi is off and you pull it to ground.<br />

In my application, this code runs after reading the I2C Real Time Clock.
