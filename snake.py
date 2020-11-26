from turtle import Turtle

move_dist=20
Up=90
Down=270
Left=180
Right=0

class Snake:
    def __init__(self):

        self.starting_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in self.starting_pos:
            self.add_segment(position)
    
    def add_segment(self,position):
        sq = Turtle(shape='square')
        sq.color('white')
        sq.penup()
        sq.goto(position)
        self.segments.append(sq)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

    def move(self):
        boxs = self.segments
        for i in range(len(boxs) - 1, 0, -1):
            # 3-2-1 //3 is storing 2's cordinates
            x = boxs[i - 1].xcor()
            y = boxs[i - 1].ycor()
            boxs[i].goto(x, y)

        self.head.forward(move_dist)

    

