# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191206
# email : suqixu@126.com
#
# 脚本功能:
# 1、文曲星上的猜数字

import random
import re
import os
import platform


# 获取一个随机数
def get_guess_number():
    number_list = list('0123456789')
    number = ''

    for i in range(4):
        rnd = random.randint(0, len(number_list) - 1)
        number += number_list[rnd]
        del number_list[rnd]

    return number


# 打印猜测结果
def print_history_list(history_list, left_cnt):
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Darwin':
        os.system('clear')

    os.system('cls')
    print('left :{}'.format(left_cnt))
    print('-' * 20)

    i = 1
    for msg in history_list:
        print('[{}] {}'.format(i, msg))
        i += 1


# 反馈猜测结果
def check_a_b(question, answer, history_list):
    a, b = 0, 0
    for x in range(4):
        for y in range(4):
            if answer[x] == question[y]:
                if x == y:
                    a += 1
                else:
                    b += 1

    history_list.append('{} => {}A{}B'.format(answer, a, b))


# 检查输入格式
def check_answer_format(answer):
    p = re.compile(r"^(\d){4}$")
    m = p.match(answer.strip())

    if m is None:
        return False

    for x in range(4):
        for y in range(4):
            if answer[x] == answer[y] and x != y:
                return False

    return True


def main():
    left_cnt = 7
    history_list = []
    question = get_guess_number()

    while True:
        if left_cnt == 0:
            left_cnt = 7
            history_list.clear()
            question = get_guess_number()

        answer = input('>>> ')

        if (answer.strip().lower() == 'exit'):
            break

        if not check_answer_format(answer):
            continue

        check_a_b(question, answer, history_list)

        print_history_list(history_list, left_cnt)

        if answer == question:
            print('[{}] => congratulations!'.format(question))
            break
        else:
            left_cnt -= 1
            if left_cnt == 0:
                print('-' * 20)
                print('[{}] => game over!'.format(question))


if __name__ == '__main__':
    main()
