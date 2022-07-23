# 让小海龟转弯
import turtle

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# 简化一下

for i in range(4):
    turtle.forward(100)
    turtle.right(90)
