import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(0)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())

def draw_line(p1,p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1,y1 = p1
    x2,y2 = p2

    for i in range(0,100 + 1,2):
        t = i/100
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        draw_point((x,y))
    pass

def draw_curve(p1,p2,p3,p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    a1x, a1y = p1
    a2x, a2y = p2
    b1x, b1y = p3
    b2x, b2y = p4

    for i in range(0,100+1,2):
        t = i/100

        ax = (1-t)*a1x + t*a2x
        ay = (1-t)*a1y + t*a2y
        draw_point((ax,ay))

        bx = (1-t)*b1x + t*b2x
        by = (1-t)*b1y + t*b2y
        draw_point((bx,by))

        if t==0.5:
            draw_line((ax,ay),(bx,by))

        cx = (1-t)*ax + t*bx
        cy = (1-t)*ay + t*by
        draw_point((cx,cy))

        pass

    pass

def draw_curve_3_points(p1, p2, p3):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)

    x1,y1 = p1; x2,y2 = p2; x3,y3 = p3

    for i in range(0,100+1,2):
        t = i/100
        x = (2 * t**2 - 3 * t + 1) * x1 + (-4 * t**2 + 4 * t) * x2 + (2 * t**2 - t) * x3
        y = (2 * t**2 - 3 * t + 1) * y1 + (-4 * t**2 + 4 * t) * y2 + (2 * t**2 - t) * y3
        draw_point((x,y))

    draw_point(p3)
    pass



def draw_curve_4_points(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        draw_point((x, y))
    draw_point(p2)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_point((x, y))
    draw_point(p3)

    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        draw_point((x, y))
    draw_point(p4)

def draw_circle(p1,p2,p3,p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        draw_point((x, y))
    draw_point(p2)

    # draw p2-p3
    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        draw_point((x, y))
    draw_point(p3)

    # draw p3-p4
    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p1[1]) / 2
        draw_point((x, y))
    draw_point(p4)

    for i in range(50, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p3[0] + (-4 * t ** 2 + 4 * t) * p4[0] + (2 * t ** 2 - t) * p1[0]
        y = (2 * t ** 2 - 3 * t + 1) * p3[1] + (-4 * t ** 2 + 4 * t) * p4[1] + (2 * t ** 2 - t) * p1[1]
        draw_point((x, y))
    draw_point(p1)
    pass

prepare_turtle_canvas()

a1 = -94,223
a2 = -158,-54
b1 = 154,-205
b2 = 131,293

#draw_line(a1,a2)
#draw_line(b1,b2)

#draw_curve_3_points((-350,-100), (-50,200), (150,-100))
#draw_curve_3_points((-50,200), (150,-100),(350,300))

draw_circle((0,100),(100,0),(0,-100),(-100,0))

turtle.done()