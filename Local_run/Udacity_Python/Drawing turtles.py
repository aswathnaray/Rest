import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    for j in range(1, 36):
        for i in range(0, 4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)

    window.exitonclick()

draw_square()