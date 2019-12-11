#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191211
# email : suqixu@126.com
#
# 脚本功能:
# 1、自动识别文本编码，对文本分词、统计词频和字数

import os

import jieba


# 识别文件编码
def get_file_encoding(file):
    encoding_list = ['gb18030', 'gbk', 'gb2312', 'utf8', 'utf16']
    file_encoding = ''
    for encoding in encoding_list:
        try:
            f = open(file, 'r', encoding=encoding)
            f.read(1024)
            file_encoding = encoding
            break
        except UnicodeDecodeError:
            pass
        finally:
            f.close()
    return file_encoding


# 对文件进行分词
def cut_file(file):
    words_count = {}
    count = 0
    file_encoding = get_file_encoding(file)
    with open(file, 'r', encoding=file_encoding) as f:
        while True:
            line = f.readline()
            if line == '':
                break

            count += len(line)  # 字数
            seg_list = jieba.cut(line)

            for word in seg_list:
                if word not in words_count.keys():
                    words_count[word] = 1
                else:
                    words_count[word] += 1
    return words_count, count


# 打印分词统计个数
def print_count(items, words_count, count, word_min_len, word_max_len, top):
    words_count_len = len(words_count)
    print('共计{}个词,{}万个字'.format(words_count_len, round(count / 10000, 2)))
    print('-' * 20)

    for i in range(words_count_len):
        word_len = len(items[i][0])
        if word_min_len <= word_len <= word_max_len:
            print(items[i])
            top -= 1
            if top <= 0:
                break


def main():
    words_count, count = cut_file(r'E:\download\红楼梦.txt')
    items = list(words_count.items())
    items.sort(key=lambda x: x[1], reverse=True)
    print_count(items, words_count, count, 2, 7, 100)


if __name__ == '__main__':
    main()
