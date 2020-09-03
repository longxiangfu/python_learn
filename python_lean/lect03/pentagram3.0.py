"""
    五角星的绘制
    lxf
    1.0
    13/3/2019
"""
import turtle

def draw_pentagram(size):
    """
        五角星的绘制
    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1;

def draw_recycle_pentagrm(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1;

    #跟新入参,并调用自身
    size += 20;
    if size <= 200:
        draw_recycle_pentagrm(size)

def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')


    size = 100
    draw_recycle_pentagrm(size)
    # while size <= 200:
    #     draw_pentagram(size)
    #     # size = size + 20
    #     size += 20

    turtle.exitonclick()

if __name__ == '__main__':
    main()
