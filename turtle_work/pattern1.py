import turtle
t=turtle.Turtle()
bg=turtle.Screen()
bg.bgcolor('black')
list1=['yellow','red','blue','green','orange','violet','purple']
for i in range(200):
    t.color(list1[i%7])
    t.pensize(i/10 +1)
    t.fd(i)
    t.lt(59)
turtle.done()