from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        for i in range(3):
            self.add_segment((-i * 20, 0))

        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def snake_size(self):
        return len(self.segments)

    def change_direction(self, direction):
        head = self.segments[0]

        if direction == "up" and self.head.heading() != 270:
            self.head.setheading(90)
        elif direction == "down" and self.head.heading() != 90:
            self.head.setheading(270)
        elif direction == "left" and self.head.heading() != 0:
            self.head.setheading(180)
        elif direction == "right" and self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        snake_size = self.snake_size() - 1
        for i in range(snake_size, -1, -1):
            curr_segment = self.segments[i]
            next_segment = self.segments[i - 1]
            if i == 0:
                curr_segment.forward(20)
            else:
                curr_segment.setposition(next_segment.position())
