import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("#f0f0f0")
    manh = turtle.Turtle()
    manh.shape("turtle")
    manh.color("#2ecc71")

    manh.forward(100)
    manh.right(90)
    manh.forward(100)
    manh.right(90)
    manh.forward(100)
    manh.right(90)
    manh.forward(100)
    manh.right(90)
    window.exitonclick()

draw_square()