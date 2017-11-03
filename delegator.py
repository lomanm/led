#!usr/bin/python
import solid # displays the color as a solid
import blink # displays the color with a blinking style
import rotate # 4 series of dots rotating around in directions counter to each other
import rotate_counter # 4 series of dots rotating around in directions counter to each other

# PARAMS
# r (red RGB value)
# g (green RGB value)
# b (blue RGB value)
# t (time in seconds, passed through to style program)
# s (the color style/animation)
def delegate(r,g,b,t,s):
    if s==1:
        solid.paint(r,g,b,t)
    elif s==2:
        blink.paint(r,g,b,t)
    elif s==3:
        rotate.paint(r,g,b,t)
    else:
        rotate_counter.paint(r,g,b,t)