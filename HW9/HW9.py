# John Schiltz
# Write any class definition of your choice that has at least two methods besides the constructor
# (it should be different from what we did in the class or the lab).
# Play with the class on IDLE by creating some objects and calling methods on them.
# Submit the program file that has the class definition and submit a screenshot of the work on IDLE.


from random import randint


class Zigfeld:
    def __init__(self, theater: str, actors: list[str]):
        self.theater = theater
        self.actors = actors

    def get_random_actors(self) -> list[str]:
        rand = [randint(0, len(self.actors)), randint(0, len(self.actors))]
        if rand[0] == rand[1]:
            rand[0] -= 1
        rand.sort()
        return self.actors[rand[0] : rand[1]]

    def change_location(self, theater: str):
        self.theater = theater

    def __str__(self) -> str:
        return f"Theater: {self.theater}\nActors: {self.actors}"


zig = Zigfeld("Brodhurst", ["Fanny Brice", "Bob Fosse", "Effel Barymore"])
print(zig)
zig.change_location("Booth")
print(f"Current theater: {zig.theater}")
actors = zig.get_random_actors()
print(f"Random cast: {actors}")

from graphics import *
from math import sqrt
from random import randint


def main():
    win = GraphWin("Circles", 500, 500)
    text1 = Text(Point(152, 20))

    # complete the rest of the program
    triangle = Polygon(Point(0,0), Point(10,0), Point(0,10) )
    triangle.setFill(color_rgb(0, 255, 0))
    triangle.draw(win)
    square = Polygon(Point(60,60), Point(70,60), Point(60,70), Point(70,70) )
    square.setFill(color_rgb(0, 0, 255))
    square.draw(win)
    circle = Circle(Point(50,50), 20)
    color = color_rgb(255, 0, 0)
    circle.setFill(color)
    circle.setOutline(color)
    circle.draw(win)

    # to end the window
    text1.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


main()
