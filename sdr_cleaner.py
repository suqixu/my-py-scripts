#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191210
# email : suqixu@126.com
#
# 脚本功能:
# 1、kindle缓存sdr目录清理

import os


class SDRCleaner:
    _root = '' # 启动目录
    _tmp_path = '' # 待删除文件临时目录
    _ignore_dirs = [] # 要忽略的目录

    def __init__(self, start_work_path, tmp_path, ignore_dirs):
        self._root = start_work_path
        self._tmp_path =  os.path.join(start_work_path, tmp_path)
        self._ignore_dirs = ignore_dirs

    def start(self):
        self._clean(self._root)

    # sdr目录是否有对应的电子书文件
    def is_exist(self, file_name):
        exts = ['.txt', '.mobi', '.pdf', '.awz3']
        for ext in exts:
            if os.path.exists(file_name + ext):
                return True
        return False

    # sdr目录清理，清理的目录放进缓存目录中
    def _clean(self, work_path):
        files = os.listdir(work_path)

        for file in files:
            os.chdir(work_path)
            if file in self._ignore_dirs or os.path.isfile(file):
                continue

            if os.path.isdir(file):
                if file.endswith('.sdr'):
                    file_name, ex = os.path.splitext(file)
                    if self.is_exist(file_name):
                        continue
                    else:
                        new_name = os.path.join(self._tmp_path, file)
                        while os.path.exists(new_name):
                            new_name += '_'

                        os.rename(file, new_name)
                        print('del =>', os.path.join(work_path, file))
                else:
                    self._clean(os.path.join(work_path, file))


def main():
    SDRCleaner(r'E:\download', 'tmp', ['g', 'tmp']).start()
    print('done!')


if __name__ == '__main__':
    main()
