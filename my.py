# x = int(input())
# if x==0:
# 	print('x is 0')
# elif (x>10):
# 	print ('x>10')
# else:
# 	print('x other')

# it = 1
# x = 0
# while x<10:
# 	print (f"Iteracia - {it}")
# 	it +=1
# 	x += 1
# 	if x>5:
# 		continue
# 	print (x)
# else:
# 	print("False")


# test = ['Hi','my','name','is']
# for word in test:
# 	print (word, len(word), sep=' ; ')


# for item in (range(5,100,20)):
# 	print (item)


# import math
#
# # print(math.sqrt(25))
# help(math)


import turtle
petr = turtle.Turtle()
petr.shape("turtle")
# petr.color('#cdcdcd')


def draw_square(dist):
	n = 4
	while n>0:
		petr.pencolor('red')
		petr.fd(dist)
		petr.left(90)
		n-=1

i =0
x=0
while i<5:
	draw_square(20)
	petr.up()
	x+=30
	petr.goto(x,0)
	petr.down()
	i+=1

petr.up()
x-=20
petr.goto(x, -30)
petr.down()

while i>0:
	x -= 30
	petr.circle(10)
	petr.up()
	petr.goto(x, -30)
	petr.down()
	i-=1

petr.up()
petr.home()
x=0
petr.goto(x, -55)
petr.down()

while i<5:
	petr.left(60)
	petr.fd(20)
	petr.right(120)
	petr.fd(20)
	petr.right(120)
	petr.fd(20)
	petr.up()
	x+=30
	petr.goto(x, -55)
	petr.down()
	i+=1


input()