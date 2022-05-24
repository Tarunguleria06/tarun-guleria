import turtle
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#FFD700")
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.goto(10,100)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#FFD700")
for i in range(5):
    turtle.forward(80)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.goto(-80,100)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#FFD700")
for i in range(5):
    turtle.forward(60)
    turtle.right(144)
turtle.end_fill()