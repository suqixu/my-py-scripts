#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191209
# email : suqixu@126.com
#
# 脚本功能:
# 1、打印日历
# 2、彩色高亮显示当前日期

import datetime


def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def get_days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28


# 彩色打印
def print_color(value, end):
    """
    \033[显示方式;前景色;背景色m要打印的文字\033[0m
    示方式: 0（默认值）、1（高亮，即加粗）、4（下划线）、7（反显）
    前景色: 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（紫色）、36（青色）、37（白色）
    背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（紫色）、46（青色）、47（白色）
    """
    print('\033[7;37;40m{}\033[0m'.format(value), end=end)


# 打印头部
def print_head(year, month):
    print('\n' + '-' * 28)
    print('{} 年 {} 月'.format(year, month))
    print('-' * 28)
    head = '日一二三四五六'
    for i in head:
        print(i, end='  ')

    print()


# 打印主体
def print_body(year, month, ignore_days):
    today = datetime.datetime.now()
    space_cnt = ignore_days
    days = get_days(year, month)

    for i in range(1, 36):
        if space_cnt > 0:
            space_cnt -= 1
            print_by_format('', i)
            continue

        show_day = i - ignore_days

        if today.year == year and today.month == month and today.day == show_day:
            print_color(show_day, end='\t')
            if i % 7 == 0:
                print('\n')
        else:
            print_by_format(show_day, i)

        if show_day == days:
            break


def print_by_format(value, index):
    print(value, end='\t')
    if index % 7 == 0:
        print()


def print_calendar(year, month):
    start_day = datetime.datetime(year, month, 1)
    ignore_days = start_day.weekday() + 1
    if ignore_days >= 7:
        ignore_days = 0

    print_head(year, month)
    print_body(year, month, ignore_days)


def main():
    year = 2019

    for i in range(1, 13):
        print_calendar(year, i)


if __name__ == '__main__':
    main()
