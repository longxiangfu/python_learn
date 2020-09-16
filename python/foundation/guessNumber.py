'''
猜数游戏
计算机随机生成一个100以内的正整数，用户通过键盘输入数字，
猜测计算机生成的随机数
注意：对用户的输入次数不限制
'''

import random

number = random.randint(1, 100)
while True:
    num_input = input('input your number:')
    if not num_input.isdigit():
        print("Your input is not a number.")
    elif int(num_input) < 1 or int(num_input) > 100:
        print('The number should between 1 and 100.')
    else:
        if int(num_input) == number:
            print('Ok')
            break
        elif int(num_input) < number:
            print('You input is less.')
        else:
            print('You input is bigger.')
