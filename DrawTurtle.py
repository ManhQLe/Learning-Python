import turtle

def draw_square(turt):
    for i in range(1,5):
        turt.forward(100)
        turt.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("#f0f0f0")
    manh = turtle.Turtle()
    manh.shape("turtle")
    manh.color("#2ecc71")

    draw_square(manh)

    tuan = turtle.Turtle()
    tuan.shape("triangle")
    tuan.color("#9b59b6")
    tuan.circle(50)
    window.exitonclick()

def draw_cirsquare():
    window = turtle.Screen()
    window.bgcolor("#f0f0f0")
    manh = turtle.Turtle()
    manh.shape("turtle")
    manh.color("#2ecc71") 
    x = int(360/10+1)
    for i in range(1,x):        
        draw_square(manh)
        manh.right(10)
    window.exitonclick()

draw_cirsquare()