"""
异常处理
"""
import traceback

while True:
    try:
        a = float(input("first number:"))
        b = float(input("second number"))
        r = a / b
        print("{0} / {1} = {2}".format(a, b, r))
        break
    except ZeroDivisionError:
        print("The second number can not b zero.try again.")
        traceback.print_exc()
    except ValueError:
        print("please enter number.try again.")
        traceback.print_exc()
    except:  # 捕捉其他异常
        traceback.print_exc()
        break
