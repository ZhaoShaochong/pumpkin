import turtle

t = turtle.Turtle()

t.pen(pencolor= "", fillcolor="orange")
t.goto(-50,0)
t.begin_fill()
t.circle(180)
t.end_fill()

t.penup()
t.fd(100)
t.pendown()

t.begin_fill()
t.circle(180)
t.end_fill()

t.penup()
t.goto(60,200)
t.pendown()

t.pen(pencolor= "black", fillcolor="black")
t.begin_fill()
t.fd(120)
t.lt(120)
t.fd(120)
t.lt(120)
t.fd(120)
t.end_fill()

t.penup()
t.goto(-60,200)
t.pendown()

t.begin_fill()
t.rt(120)
t.fd(120)
t.lt(120)
t.fd(120)
t.lt(120)
t.fd(120)
t.end_fill()

t.penup()
t.goto(0,200)
t.pendown()

t.begin_fill()
t.rt(120)
t.fd(70)
t.lt(120)
t.fd(70)
t.lt(120)
t.fd(70)
t.end_fill()

t.penup()
t.goto(0,50)
t.pendown()


t.begin_fill()
t.rt(120)
t.fd(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(100)
t.end_fill()

