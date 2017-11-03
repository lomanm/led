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
    frameTime = .1 # the number of seconds for each frame
    iterations = int(round(t/frameTime, 0))
    unicorn.off()                # turn off all of the led's
    
    # vars used for the 2nd inner most circle
    c2LeadingX = 4;
    c2LeadingY = 2;
    c2TrailingX = 2;
    c2TrailingY = 5;
    
    # vars used for the 3rd inner most circle
    c3LeadingX = 5;
    c3LeadingY = 1;
    c3TrailingX = 1;
    c3TrailingY = 1;
    
    # vars used for the 4th inner most circle
    c4LeadingX = 0;
    c4LeadingY = 6;
    c4TrailingX = 0;
    c4TrailingY = 0;

    for i in range(iterations):

        # handle the inner circle (1 of 4), clockwise
        if i%4==0:
            unicorn.set_pixel(4,4,r,g,b) # turn one led on
            unicorn.set_pixel(4,3,0,0,0) # turn one led off
        elif i%4==1:
            unicorn.set_pixel(3,4,r,g,b) # turn one led on
            unicorn.set_pixel(4,4,0,0,0) # turn one led off
        elif i%4==2:
            unicorn.set_pixel(3,3,r,g,b) # turn one led on
            unicorn.set_pixel(3,4,0,0,0) # turn one led off
        else:
            unicorn.set_pixel(4,3,r,g,b) # turn one led on
            unicorn.set_pixel(3,3,0,0,0) # turn one led off
            
        # handle the 2nd inner most circle (2 of 4), counter-clockwise
        if i==0:
            unicorn.set_pixel(4,2,r,g,b) # turn eight led's on to start
            unicorn.set_pixel(5,2,r,g,b) 
            unicorn.set_pixel(5,3,r,g,b) 
            unicorn.set_pixel(5,4,r,g,b)
            unicorn.set_pixel(5,5,r,g,b)
            unicorn.set_pixel(4,5,r,g,b)
            unicorn.set_pixel(3,5,r,g,b)
            unicorn.set_pixel(2,5,r,g,b)
        else:
            unicorn.set_pixel(c2TrailingX,c2TrailingY,0,0,0) # turn off the trailing led
            if 5 <= (c2LeadingX+c2LeadingY) <= 10 and c2LeadingX >= c2LeadingY: # going down
                if c2LeadingY == 2:
                    c2LeadingX -= 1 # iterate the leading X value
                else:
                    c2LeadingY -= 1 # iterate the leading Y value
            else: # going up
                if c2LeadingY == 5:
                    c2LeadingX += 1 # iterate the leading X value
                else:
                    c2LeadingY += 1 # iterate the leading Y value
                    
            unicorn.set_pixel(c2LeadingX,c2LeadingY,r,g,b) # turn on the new leading led
            if 5 <= (c2TrailingX+c2TrailingY) <= 10 and c2TrailingX >= c2TrailingY: # going down
                if c2TrailingY == 2:
                    c2TrailingX -= 1 # iterate the trailing X value
                else:
                    c2TrailingY -= 1 # iterate the trailing Y value
            else: # going up
                if c2TrailingY == 5:
                    c2TrailingX += 1 # iterate the trailing X value
                else:
                    c2TrailingY += 1 # iterate the trailing Y value
                    
        # handle the 3rd inner most circle (3 of 4), clockwise
        if i==0:
            unicorn.set_pixel(1,1,r,g,b) # turn five led's on to start
            unicorn.set_pixel(2,1,r,g,b)
            unicorn.set_pixel(3,1,r,g,b)
            unicorn.set_pixel(4,1,r,g,b)
            unicorn.set_pixel(5,1,r,g,b)
        else:
            unicorn.set_pixel(c3TrailingX,c3TrailingY,0,0,0) # turn off the trailing led
            if 3 <= (c3LeadingX+c3LeadingY) <= 12 and c3LeadingX <= c3LeadingY: # going down
                if c3LeadingX == 1:
                    c3LeadingY -= 1 # iterate the leading Y value
                else:
                    c3LeadingX -= 1 # iterate the leading X value
            else: # going up
                if c3LeadingX == 6:
                    c3LeadingY += 1 # iterate the leading Y value
                else:
                    c3LeadingX += 1 # iterate the leading X value
                    
            unicorn.set_pixel(c3LeadingX,c3LeadingY,r,g,b) # turn on the new leading led
            if 3 <= (c3TrailingX+c3TrailingY) <= 12 and c3TrailingX <= c3TrailingY: # going down
                if c3TrailingX == 1:
                    c3TrailingY -= 1 # iterate the trailing Y value
                else:
                    c3TrailingX -= 1 # iterate the trailing X value
            else: # going up
                if c3TrailingX == 6:
                    c3TrailingY += 1 # iterate the trailing Y value
                else:
                    c3TrailingX += 1 # iterate the trailing X value

        # handle the 4th inner most circle (4 of 4), counter-clockwise
        if i==0:
            unicorn.set_pixel(0,0,r,g,b) # turn seven led's on to start
            unicorn.set_pixel(0,1,r,g,b) 
            unicorn.set_pixel(0,2,r,g,b) 
            unicorn.set_pixel(0,3,r,g,b)
            unicorn.set_pixel(0,4,r,g,b)
            unicorn.set_pixel(0,5,r,g,b)
            unicorn.set_pixel(0,6,r,g,b)
        else:
            unicorn.set_pixel(c4TrailingX,c4TrailingY,0,0,0) # turn off the trailing led
            if 1 <= (c4LeadingX+c4LeadingY) <= 14 and c4LeadingX >= c4LeadingY: # going down
                if c4LeadingY == 0:
                    c4LeadingX -= 1 # iterate the leading X value
                else:
                    c4LeadingY -= 1 # iterate the leading Y value
            else: # going up
                if c4LeadingY == 7:
                    c4LeadingX += 1 # iterate the leading X value
                else:
                    c4LeadingY += 1 # iterate the leading Y value
                    
            unicorn.set_pixel(c4LeadingX,c4LeadingY,r,g,b) # turn on the new leading led
            if 1 <= (c4TrailingX+c4TrailingY) <= 14 and c4TrailingX >= c4TrailingY: # going down
                if c4TrailingY == 0:
                    c4TrailingX -= 1 # iterate the trailing X value
                else:
                    c4TrailingY -= 1 # iterate the trailing Y value
            else: # going up
                if c4TrailingY == 7:
                    c4TrailingX += 1 # iterate the trailing X value
                else:
                    c4TrailingY += 1 # iterate the trailing Y value
        
        unicorn.show()
        time.sleep(frameTime)

