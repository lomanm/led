#!usr/bin/python
import unicornhat as unicorn
import time

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

    for x in range(width):
        for y in range(width):
          unicorn.set_pixel(x,y,r,g,b)
          
    unicorn.show()
    time.sleep(t)