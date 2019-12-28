# -*- coding:utf-8 -*-

import os

def rename(path):
    files = os.listdir(path)
    for file in files:
        words = [
            '[阳光电影www.ygdy8.com].',
            '[电影天堂www.dy2018.com]',
            '[阳光电影www.ygdy8.net].',
            'BD','HD','字幕','国语',
            '中字','高清','国英','双字',
            '日语','双语','国粤','电影版',
            '中英','720p','.双.','中文',
            '720P','1080p','1280','日粤',
            '韩版','导演','加长版','真人版',
            '粤语','韩语', '英语','美版',
            '原盘','剪辑',
            '阳光电影www.ygdy8.com.',
            '阳光电影www.ygdy8.net.',
            '[电影天堂www.dygod.com]',
            '.[日]东野圭吾.中亚',
            '.[日]东野圭吾',
            '.好读',
            '《',
            '》'
            ]

        newfile = file
        for word in words:
            newfile = newfile.replace(word, '') 

        for i in list(range(2)):
            newfile = newfile.replace('..', '.') 

        if file != newfile:
            os.rename(os.path.join(path,file), os.path.join(path,newfile))
            print(newfile)
    
    print('done!')

def main():
    dirs = [
        #'/Users/suqixu/Movies',
        #'/Volumes/suqixu/m',
        #'/Volumes/zzy/_/movie'
        #'/Volumes/zzy/_',
        #'/Volumes/sqx'
        '/Users/suqixu/Downloads/azw3/未命名文件夹'
        ]
    
    for path in dirs:
        rename(path)

if __name__ == '__main__':
    main()
