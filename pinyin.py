#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191208
# email : suqixu@126.com
#
# 脚本功能:
# 1、游戏文件批量转拼音

import os
from xpinyin import Pinyin


# 游戏文件批量转拼音重命名
def file2pinyin(work_path):
    files = os.listdir(work_path)
    p = Pinyin()

    for file in files:
        os.chdir(work_path)
        if os.path.isfile(file):
            file_name, ext = os.path.splitext(file)
            py = p.get_pinyin(file_name)
            new_file = py + ext
            new_file = new_file.replace('-：-', '：')
            if file.startswith('._'):
                os.remove(file)
                print('del =>', file)
            elif file != new_file:
                os.rename(file, new_file)
                print(file, '==>', new_file)
        elif os.path.isdir(file):
            new_dir = p.get_pinyin(file)
            os.rename(file, new_dir)
            file2pinyin(os.path.join(work_path, new_dir))


def main():
    work_path = r'/Volumes/SUQIXU_128G/roms'
    if os.path.exists(work_path):
        file2pinyin(work_path)

    print('done!')


if __name__ == '__main__':
    main()
