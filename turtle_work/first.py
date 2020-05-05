import turtle
t=turtle.Turtle()
bg=turtle.Screen()
bg.bgcolor('brown')
t.color('blue','green')
t.shape('turtle')
t.speed(1)
t.begin_fill()
t.fillcolor('red')
t.pensize(20)
t.circle(100)
t.end_fill()

t.goto(0,-100)
t.hideturtle()

turtle.done()