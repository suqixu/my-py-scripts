#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191129
# email : suqixu@126.com
#
# 脚本功能:
# 1、存档文件解析统计

import re
import os

group_stack = []
group_count = {}

def main():
    path =  r'D:\data\nutstore\wiki\生活\归档'
    file_name_list = os.listdir(path)
    for file_name in file_name_list:


        try:
            f = open(os.path.join(path, file_name), 'r', encoding='utf-8')
            while True:
                line = f.readline()
                if line == '':
                    break
                else:
                    line = line.strip()
                    if line == '':
                        group_stack.pop()

                    p = re.compile(r"\[(.*)\]")
                    m = p.match(line)
                    if m is not None:
                        group_name = m.group(1)
                        group_stack.append(group_name)
                        group_count.setdefault(group_name, 0)
                    else:
                        if len(group_stack) == 0:
                            continue

                        p = re.compile(r"[^\d]+(\d+)-(\d+)(\s)*$")
                        m = p.match(line)
                        if m is not None:
                            print('{} ==> {}'.format(group_name, line))
                            group_count[group_stack[0]] += (int(m.group(2)) - int(m.group(1)) + 1)
                        else:
                            group_count[group_stack[0]] += 1

                        #print(group_count[group_stack[0]])
                    #print(line)

            total = 0
            for i in group_count:
                total+= group_count[i]
                print('{}:{}'.format(i, group_count[i]))
            print('-'* 10)
            print('共计:' + str(total) + '\n')
            group_count.clear()
            group_stack.clear()
        except Exception as ex:
            print(ex)
        finally:
            f.close()

if __name__ == '__main__':
    main()