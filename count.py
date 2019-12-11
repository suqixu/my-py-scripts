#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191204
# email : suqixu@126.com
#
# 脚本功能:
# 1、存档文件解析统计

import re
import os


def total_print(file_name, group_stack, group_count):
    group_list = list(group_count.items())
    group_list.sort(key=lambda x: x[1], reverse=True)

    list_len = len(group_list)
    total = 0
    total_name = os.path.splitext(file_name)[0]

    for i in range(list_len):
        item = group_list[i]
        print('{} {}:{}'.format(i + 1, item[0], item[1]))
        total += item[1]

    print('-' * 20)
    print('{}:{}\n'.format(total_name, total))

    group_stack.clear()
    group_count.clear()


def get_group_name(line):
    p = re.compile(r"\[(.*)\]")
    m = p.match(line)

    if m is not None:
        return m.group(1)
    else:
        return ''


def total_line_count(line, group_stack, group_count):
    p = re.compile(r"[^\d]+(\d+)-(\d+)(\s)*$")
    m = p.match(line)
    key = group_stack[0]

    if m is not None:
        start_index = int(m.group(1))
        end_index = int(m.group(2))
        group_count[key] += (end_index - start_index + 1)
    else:
        group_count[key] += 1


def total_line(line, group_stack, group_count):
    line = line.strip()
    if line == '':
        group_stack.pop()

    group_name = get_group_name(line)
    if group_name != '':
        group_stack.append(group_name)
        group_count.setdefault(group_name, 0)
    else:
        if len(group_stack) != 0:
            total_line_count(line, group_stack, group_count)


def total_file(path, file_name, group_stack, group_count):
    f = open(os.path.join(path, file_name), 'r', encoding='utf-8')
    while True:
        line = f.readline()
        if line == '':
            break
        else:
            total_line(line, group_stack, group_count)
    f.close()


def main():
    group_stack = []
    group_count = {}
    path = r'D:\data\nutstore\wiki\生活\归档'
    file_name_list = os.listdir(path)

    for file_name in file_name_list:
        total_file(path, file_name, group_stack, group_count)
        total_print(file_name, group_stack, group_count)


if __name__ == '__main__':
    main()
