#!usr/bin/python
import unicornhat as unicorn
import time
import math

# PARAMS
# r (red RGB value)
# g (green RGB value)
# b (blue RGB value)
# t (total time in seconds for this animation/style)
def paint(r,g,b,t):
    unicorn.set_layout(unicorn.HAT)
    unicorn.rotation(0)
    unicorn.brightness(0.5)
    width,height=unicorn.get_shape()
    blinkTime = .25 # .25 is the amount of seconds of the blink (open and closed)
    iterations = int(round(t/blinkTime, 0))
    showColor = True #
    unicorn.off()                # turn off all of the led's
    
    for i in range(iterations):
        for x in range(width):
            for y in range(width):
                if showColor:
                    unicorn.set_pixel(x,y,r,g,b) # display the color
                else:
                    unicorn.off()                # turn off the color
            
        unicorn.show()
        time.sleep(blinkTime)
        showColor = not showColor # toggle the boolean value