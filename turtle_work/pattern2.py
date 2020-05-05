import turtle
t=turtle.Turtle()
list1=['yellow','blue','red','green']
bg=turtle.Screen()
bg.bgcolor('black')
t.color('yellow')
t.speed(0)
t.pensize(2)
for i in range(72):
    t.color(list1[i%len(list1)])
    t.circle(100,steps=4)
    t.left(5)

turtle.done()