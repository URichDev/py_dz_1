import turtle

tur = turtle.Turtle()
tur.screen.bgcolor('#B4B40A')
tur.left(90)

def draw_line(x, dist): # dist - angle of rotation
    tur.fd(x)
    tur.right(dist)

i = 0
x = 350 #What is the length of the first line
while i<15:
    draw_line(x, 105)
    x = 3 * x / 4
    i += 1

tur.up()
tur.home()

input()