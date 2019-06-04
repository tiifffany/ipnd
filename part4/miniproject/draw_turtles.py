import turtle

window = turtle.Screen()
window.bgcolor("orange")

sam = turtle.Turtle()
sam.shape("turtle")
sam.color("black")
sam.speed(30)

def draw_squares():
    step = 0
    square = 4
    while  step < square:
        sam.forward(100)
        sam.right(90)
        step +=1

draw_squares()

squares = 0
circle = 36
while squares < circle:
    sam.right(10)
    draw_squares()
    squares +=1

sam.right(90)
sam.forward(300)


window.exitonclick()
