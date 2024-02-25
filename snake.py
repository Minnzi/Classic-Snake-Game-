from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        start_x = 0
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setx(start_x)
            self.snake.append(segment)
            start_x -= 20

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            self.snake[seg_num].goto(self.snake[seg_num - 1].pos())
        self.head.fd(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    # def right(self):
    #     if self.snake[1].ycor() > self.snake[0].ycor():
    #         self.snake[0].lt(90)
    #     else:
    #         self.snake[0].rt(90)
    #
    # def left(self):
    #     if self.snake[1].ycor() > self.snake[0].ycor():
    #         self.snake[0].rt(90)
    #     else:
    #         self.snake[0].lt(90)
    #
    # def up(self):
    #     if self.snake[1].xcor() > self.snake[0].xcor():
    #         self.snake[0].rt(90)
    #     else:
    #         self.snake[0].lt(90)
    #
    # def down(self):
    #     if self.snake[1].xcor() > self.snake[0].xcor():
    #         self.snake[0].lt(90)
    #     else:
    #         self.snake[0].rt(90)

