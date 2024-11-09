import turtle
import random
class draw:
    def __init__(self,num_sides):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = 0.618

    def draw_polygon(self):
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()


    def reset(self):
        turtle.penup()
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= self.reduction_ratio


    def draw_nested_polygons(self):
        for i in range(3):
            self.draw_polygon()
            self.reset()

# class tri(draw):
#     def __init__(self):
#         # Call the __init__ method of the parent class, and specify that the number of sides is 3 for a triangle
#         super().__init__(3)

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
turtle.penup()

n = int(input("Enter choice 1-9\n"))

if n>=1 and n<=3: # choice 1-3
    for i in range(20):
        x = draw(n+2)
        x.draw_polygon()
        x.reset()
        turtle.update()

if n==4: #choice 4
    for i in range(20):
            x = draw(random.randint(3, 5))
            x.draw_polygon()
            x.reset()
            turtle.update()

if n >=5 and n<=7: #choice 5-7
    for i in range(20):
        x = draw(n-2)
        x.draw_polygon()
        x.draw_nested_polygons()


if n==8: #choice 8
    for i in range(20):
            x = draw(random.randint(3, 5))
            x.draw_polygon()
            x.draw_nested_polygons()
            turtle.update()

if n==9: #choice 9
    for i in range(5):
            x = draw(4)
            y = draw(3)
            z = draw(random.randint(3, 5))
            x.draw_polygon()
            y.draw_polygon()
            z.draw_polygon()
            z.draw_nested_polygons()

turtle.done()















# draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = get_new_color()
# border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
# reduction_ratio = 0.618

# reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.left(90)
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.right(90)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
# size *= reduction_ratio

# draw the second polygon embedded inside the original
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# hold the window; close it by clicking the window close 'x' mark
# turtle.done()