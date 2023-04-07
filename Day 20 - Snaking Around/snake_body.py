from turtle import Turtle


class Snake:
    def __init__(self, initial_positions):
        self.segments = []
        self.create_snake(initial_positions)
        self.head = self.segments[0]
        self.is_alive = True

    def create_snake(self, starting_positions):
        for position in starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.seth(0)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=position[0], y=position[1])
            new_segment.showturtle()
            self.segments.append(new_segment)

    def add_segment(self):
        # new_segment = Turtle(shape="square", visible=False)
        # new_segment.speed(0)
        # new_segment.color("white")
        # new_segment.penup()
        # new_segment.goto(self.tail.xcor(), self.tail.ycor())
        # new_segment.showturtle()
        tail = self.segments[-1]
        new_segment = tail.clone()
        self.segments.append(new_segment)
        # self.segment_positions.append(new_segment.pos())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
            # self.segment_positions[segment] = self.segments[segment].pos()
        self.head.forward(20)

    def hide(self):
        for segment in self.segments:
            segment.hideturtle()

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def get_segment_positions(self):
        segment_positions = []
        for segment in self.segments:
            segment_positions.append(segment.position())
        return segment_positions
