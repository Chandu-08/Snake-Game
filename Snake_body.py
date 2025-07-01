from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(20,0)]
MOVE_DISTANCE=20
UP=90
RIGHT=0
DOWN=270
LEFT=180
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)
    # Add a new segment to the snake when ever it eats the food
    def extend(self):
      self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range((len(self.segments)-1),0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def move_up(self):
     if self.segments[0].heading()!=DOWN:
        self.segments[0].setheading(UP)

    def move_down(self):
        if self.segments[0].heading() != UP:
         self.segments[0].setheading(DOWN)

    def move_right(self):
        if self.segments[0].heading() != LEFT:
         self.segments[0].setheading(RIGHT)

    def move_left(self):
        if self.segments[0].heading() != RIGHT:
         self.segments[0].setheading(LEFT)

