# Oscilloscope Plotter
**R2R Parallel Port Acess Oscilloscope Plotter**

This project uses an STM32F103("Blue Pill") or Arduino Uno/Nano to draw images on an oscilloscope using the XY mode.

Neither microcontroller development board has a built-in DAC, but they do have enough output pins to make use of a simple R2R DAC. 



**Arduino UNO/NANO**

The Arduino UNO does not allow for full output writing of PORTB. This port is limited to only 6-bits according to the documentation. This means you will have to use one 8-bit R2R DAC and one 6-bit R2R DAC. 

Although this saves some resistors, it slightly distorts the image due to scaling down the y-output down to 6-bits rather than 8. 



**STM32F103xx(aka "Blue Pill")**

The STM32F103xx blue pill micrcontroller is better for this application since it allows for a true dual 8-bit parallel output. It also has a faster clock speed than the Arduino Uno/Nano which means there are more total bits per second. This results in plotting slightly more detailed images and less distortion due to scaling. 

Here I use the lower 8 bits of PORTA and the upper 8 bits of PORTB. The reason for choosing the upper 8 bits of PORTB rather than the lower 8 was because some of the lower bits did not seem to be writeable.


**Drawing tool**

I made a drawing tool using tkinter on  Python 3. Although it logs up to the maximum amount of points in a 255x255 window, both microcontrollers cannot output all data poiints. The STM32 can output about 500 and Arduino Uno about 250. 
