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
    :param size:
    :return:
    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1;

def main():
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')


    size = 100
    while size <= 200:
        draw_pentagram(size)
        # size = size + 20
        size += 20

    turtle.exitonclick()

if __name__ == '__main__':
    main()
