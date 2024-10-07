from turtle import Turtle
STARTING_POSITIONS =[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
          self.add_seg(pos)
    def extend(self):
        self.add_seg(self.segments[-1].pos())

    def add_seg(self,pos):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.segments.append(snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_cordinate = self.segments[seg_num - 1].xcor()
            new_y_cordinate = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_cordinate, new_y_cordinate)
        self.head.forward(MOVE_DISTANCE)


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
