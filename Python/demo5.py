# 科赫雪花
import turtle


def kehe(len, n):
    if n == 0:
        turtle.fd(len)
    else:
        for i in [0, 60, -120, 60]:
            turtle.left(i)
            kehe(len / 3, n - 1)


lenth = 500
level = 3
du = 120


def main():
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pensize(2)
    turtle.color('green')
    turtle.pendown()
    kehe(lenth, level)
    turtle.right(du)
    kehe(lenth, level)
    turtle.right(du)
    kehe(lenth, level)
    turtle.right(du)
    turtle.hideturtle()
    turtle.done()


main()
