from turtle import Turtle


class Player:
    def __init__(self, xcor, ycor, state):
        self.new_turtle = Turtle()
        self.new_turtle.color("black")
        self.new_turtle.hideturtle()
        self.new_turtle.penup()
        self.new_turtle.setposition(xcor, ycor)
        self.new_turtle.write(state, False, "center", ("Courier", 9, "normal"))

    def game_over():
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.setposition(0, 0)
        new_turtle.write("You Win!", False, "center", ("Courier", 30, "normal"))


