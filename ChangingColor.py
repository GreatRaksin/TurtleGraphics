import turtle

tina = turtle.Turtle()
tina.shape('turtle')

ws = turtle.Screen()

tina.pensize(3)
tina.speed(10)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "cyan"]

for each_color in colors:
    angle = 360 / len(colors)
    tina.color(each_color)
    tina.circle(40)
    tina.right(angle)
    tina.forward(30)

ws.exitonclick()
