from graphics import *
from math import sqrt
from random import randint


def main():
    win = GraphWin("Circles", 500, 500)
    text1 = Text(Point(152, 20), "How many circles do you want to draw:")
    text2 = Text(Point(120, 60), "Click anywhere after entering.")
    text1.draw(win)
    text2.draw(win)
    nbox = Entry(Point(40, 40), 4)
    nbox.draw(win)

    win.getMouse()
    n = int(nbox.getText())

    text2.undraw()
    nbox.undraw()

    text1.setText("Click twice to draw each circle.")

    # complete the rest of the program
    for _ in range(n):
        click_1 = win.getMouse()
        click_2 = win.getMouse()

        distance = sqrt(
            ((click_1.getX() - click_2.getX()) ** 2)
            + ((click_1.getY() - click_2.getY()) ** 2)
        )
        circle = Circle(click_1, distance)
        color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
        circle.setFill(color)
        circle.setOutline(color)
        circle.draw(win)

    # to end the window
    text1.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


main()
