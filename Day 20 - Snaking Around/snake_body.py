from turtle import Turtle


class Snake:
    def __init__(self, initial_positions: list[tuple[int, int]]):
        self.positions: list[tuple[int, int]] = initial_positions
        self.segments: list[Turtle] = []
        self.create_snake(initial_positions)
        self.head: Turtle = self.segments[0]
        self.is_alive: bool = True

    def create_snake(self, starting_positions: list[tuple[int, int]]) -> None:
        for position in starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=position[0], y=position[1])
            self.segments.append(new_segment)

    def add_segment(self):
        tail = self.segments[-1]
        new_segment = tail.clone()
        self.segments.append(new_segment)

    def move(self):
        # Update the positions list
        self.positions = [  # type: ignore
            (self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
            for i in range(1, len(self.segments))
        ]

        # Move the segments
        for i, segment in enumerate(self.segments[1:], start=1):
            segment.goto(self.positions[i - 1])

        self.head.forward(20)

    def up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)

    def get_segment_positions(self):
        return self.positions
