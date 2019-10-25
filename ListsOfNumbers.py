import turtle

tina = turtle.Turtle()
tina.shape('turtle')

screen = turtle.Screen()

tina.pensize(2)
tina.speed(50)

number_list = range(1, 50)

tina.color("green")
for number in number_list:
    tina.forward(number * 2)
    tina.left(60)

screen.exitonclick()
