"""
异常处理
"""

while True:
    try:
        a = float(input("first number:"))
        b = float(input("second number"))
        r = a / b
        print("{0} / {1} = {2}".format(a, b, r))
        break
    except ZeroDivisionError:
        print("The second number can not b zero.try again.")
    except ValueError:
        print("please enter number.try again.")
    except:  # 捕捉其他异常
        break
