import turtle
tur = turtle.Turtle()
tur.screen.bgcolor('#B4B40A')

tur1 = turtle.Turtle()
tur2 = turtle.Turtle()
tur3 = turtle.Turtle()
tur4 = turtle.Turtle()

tur1.speed(8)
tur2.speed(8)
tur3.speed(8)
tur4.speed(8)

def draw_square(x, dist): # x- side length of a square; dist - number of turns in a spiral
    # draw square
    tur.up()
    tur.setx(-x / 2)
    tur.sety(- x / 2)
    tur.down()
    i=0
    while i<4:
        tur.fd(x)
        tur.left(90)
        i+=1
    #draw lines
    step = x/(2*(dist+1))

    tur1.up()
    tur1.setx(x/2-step)
    tur1.sety(x/2)
    tur1.right(90)
    tur1.down()

    tur2.up()
    tur2.setx(-x / 2)
    tur2.sety(x / 2 - step)
    tur2.down()

    tur3.up()
    tur3.setx(-x / 2 + step)
    tur3.sety(-x / 2)
    tur3.left(90)
    tur3.down()

    tur4.up()
    tur4.setx(x / 2)
    tur4.sety(-x / 2 + step)
    tur4.left(180)
    tur4.down()

    i=dist
    j = x/step

    while i>=0:
        if j==2:
            length = step
        else:
            length = (j-2) * step
        tur1.fd(length)
        tur1.right(90)

        tur2.fd(length)
        tur2.right(90)

        tur3.fd(length)
        tur3.right(90)

        tur4.fd(length)
        tur4.right(90)

        i-=1
        j-=2


draw_square(220,10)

input()
