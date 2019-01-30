# Lab No. 3
# CTEC 121
# Jeb Gipson

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    Circle1 = Circle(Point(500,600), 150)
    Circle1.draw(win)
    Circle2 = Circle(Point(500,375), 100)
    Circle2.draw(win)
    Circle3 = Circle(Point(500,225), 50)
    Circle3.draw(win)

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eye1 = Circle(Point(475,215), 10)
    eye1.draw(win)

    eye2 = eye1.clone()
    eye2.move(45,0)
    eye2.draw(win)


    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
    nose = Polygon(Point(470,246), Point(610,246), Point(490,226))
    nose.setFill("Orange")
    nose.draw(win)



    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = Rectangle(Point(440, 180), Point(550,100))
    hat.setFill('Black')
    hat.draw(win)



    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    hatline = Line(Point(400, 180), Point(580,180))
    hatline.draw(win)



    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()