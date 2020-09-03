"""
    五角星的绘制
    lxf
    1.0
    13/3/2019
"""
import turtle

def main():
    count = 1
    while count <= 5:
        turtle.forward(100)
        turtle.right(144)
        count = count + 1

    turtle.exitonclick()

if __name__ == '__main__':
    main()
