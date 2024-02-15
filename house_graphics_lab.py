# =============================================================================
# Program: House Lab
# Author: josh wild
# Description: spaceship house lab
# Version: 1.0
# Date Modified: 1/12/2022
# =============================================================================
# Import Libraries
from graphics import *
import time
import random

# =============================================================================
# Global Variables/Constants
window = GraphWin("My House", 1000, 700)

# =============================================================================
# User-Defined Functions
def drawBase(x, x2, y, y2, color):
    """Draws the main rectangle of the house."""
    hBase = Rectangle(Point(x, y), Point(x2, y2))
    hBase.setFill(color)
    hBase.setOutline(color)
    hBase.draw(window)
    front = Arc(Point(x + 152, y), Point(x - 150, y2), 90, 180, "sector")
    front.setFill("light blue")
    front.setOutline("white")
    front.draw(window)

def drawWings(x1, y1, x2, y2, x3, y3, color):
    """Draws the wings of the spaceship and can be used to make other triangles"""
    wing = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    wing.setFill(color)
    wing.setOutline(color)
    wing.draw(window)

def drawDoor(x1, x2, y1, y2, color):
    """"Draws the door of the house."""
    doorRec = Rectangle(Point(x1, y1), Point(x2, y2))
    doorRec.setFill(color)
    doorRec.setOutline(color)
    doorRec.draw(window)
    topDoor = Arc(Point(x1, y2 - 25), Point(x2, y1 - (x2 - x1)), 0, 180, "sector")
    topDoor.setFill(color)
    topDoor.setOutline(color)
    topDoor.draw(window)
    handle = Circle(Point(x1 + 15, y2 - 50), 5)
    handle.setFill("black")
    handle.draw(window)

def drawStars():
    """draw stars in background"""
    for i in range(150):
        star = Circle(Point(random.randrange(0, 1001), random.randrange(0, 701)), random.randrange(1, 4))
        star.setFill("white")
        star.setOutline("white")
        star.draw(window)


def drawChimney():
    """draws chimney/exhaust pipe on spaceship"""
    chimFire = Polygon(Point(835, 253), Point(885, 260), Point(835, 267))
    chimFire.setFill("red")
    chimFire.setOutline("red")
    chimFire.draw(window)
    chimFire = globals()
    chimney = Line(Point(620, 300), Point(700, 260))
    chimney.setFill("light gray")
    chimney.setWidth(10)
    chimney.draw(window)
    chimney2 = Line(Point(699, 260), Point(835, 260))
    chimney2.setFill("light gray")
    chimney2.setWidth(9)
    chimney2.draw(window)


def drawFire():
    """draws fire coming out of bottom of spaceship"""
    fire1 = Polygon(Point(790, 300), Point(1000, 390), Point(790, 480))
    fire1.setFill("red")
    fire1.setOutline("red")
    fire1.draw(window)
    fire2 = Polygon(Point(790, 270), Point(950, 330), Point(790, 390))
    fire2.setFill("orange")
    fire2.setOutline("orange")
    fire2.draw(window)
    fire3 = Polygon(Point(790, 390), Point(950, 450), Point(790, 510))
    fire3.setFill("orange")
    fire3.setOutline("orange")
    fire3.draw(window)
    fire4 = Polygon(Point(790, 340), Point(925, 390), Point(790, 440))
    fire4.setFill("yellow")
    fire4.setOutline("yellow")
    fire4.draw(window)


def drawRoof():
    """Draws the roof of the house."""
    roof = Polygon(Point(315, 290), Point(390, 265), Point(540, 265), Point(615, 290))
    roof.setFill("white")
    roof.draw(window)

def drawCircularWindow(x, y, r, color):
    """Draws a window with the upper left hand corner at (x,y)."""
    circ = Circle(Point(x, y), r)
    circ.setFill(color)
    circ.draw(window)
    cross1 = Line(Point(x + r, y), Point(x - r, y))
    cross1.setFill("black")
    cross1.setWidth(1.1)
    cross1.draw(window)
    cross2 = Line(Point(x, y + r), Point(x, y - r))
    cross2.setFill("black")
    cross2.setWidth(1.1)
    cross2.draw(window)

def drawSquareWindow(x, y, size, color):
    """Draw a square window with the side lengths of x and y"""
    sqWindow = Rectangle(Point(x, y), Point(x + size, y + size))
    sqWindow.setFill(color)
    sqWindow.draw(window)
    sqCross1 = Line(Point(x, y + size/2), Point(x + size, y + size/2))
    sqCross1.setFill("black")
    sqCross1.setWidth(1.1)
    sqCross1.draw(window)
    sqCross2 = Line(Point(x + size/2, y), Point(x + size/2, y + size))
    sqCross2.setFill("black")
    sqCross2.setWidth(1.1)
    sqCross2.draw(window)


# =============================================================================
# Main Function
def main():
    """This is the main function for the program."""

# set background
    window.setBackground("black")
# call all functions
    drawStars()
    drawFire()
    drawRoof()
    drawWings(700, 290, 800, 290, 800, 190, "white")
    drawWings(700, 490, 800, 490, 800, 590, "white")
    drawChimney()
    drawBase(200, 800, 290, 490, "white")
    drawDoor(250, 300, 375, 450, "light blue")
    drawCircularWindow(375, 390, 30, "light blue")
    drawCircularWindow(475, 390, 30, "light blue")
    drawCircularWindow(575, 390, 30, "light blue")
    drawCircularWindow(675, 390, 30, "light blue")

# shooting star animation
    while window.isOpen():
        star0 = Line(Point(550, 100), Point(540, 105))
        star0.setFill("white")
        star0.setWidth(3)
        star0.draw(window)
        time.sleep(.03)
        star0.undraw()
        star0 = Line(Point(540, 105), Point(520, 115))
        star0.setFill("white")
        star0.setWidth(3)
        star0.draw(window)
        time.sleep(.03)
        star0.undraw()
        star0 = Line(Point(520, 115), Point(480, 135))
        star0.setFill("white")
        star0.setWidth(3)
        star0.draw(window)
        time.sleep(.03)
        star0.undraw()
        time.sleep(random.randrange(5, 13))



    # Pause before ending the program.
    window.getMouse()
    window.close()


# =============================================================================
# Call the Main Function to Start the Program
main()
