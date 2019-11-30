# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191128
# email : suqixu@126.com
#
# 脚本功能:
# 1、根据文件md5识别重复文件
# 2、批量分类图片和视频文件
# 3、按指定格式对文件批量重命名

import os
import datetime
import re
import hashlib


# 如果目录不存在，则创建
def mkdir_if(paths):
    for p in paths:
        if not os.path.exists(p):
            os.mkdir(p)
            print("create dir: {}".format(p))


# 按文件扩展名移动文件
def move_by_ext(src_path, desc_path, file, ext_list):
    ext = os.path.splitext(file)[1]
    if ext.lower() in ext_list:
        src = os.path.join(src_path, os.path.basename(file))
        desc = os.path.join(desc_path, file)
        os.rename(src, desc)
        print('move file:{} => {}'.format(src, desc))


# 将文件按类型分组
def group(files, src_path, v_path, p_path):
    for file in files:
        move_by_ext(src_path, v_path, file, ['.mp4'])
        move_by_ext(src_path, p_path, file, ['.jpg', '.png'])


# 按前缀 + yymmdd + 自增序号 + 小写的文件扩展名格式给文件命名
# 可以识别断掉的自增编号，更正为连续编号
def rename_if(pre, path, file, index, file_cnt):
    file_name, ext = os.path.splitext(file)

    if file_name == '.DS_Store':
        return

    p = re.compile(pre + r"(\d+)")
    m = p.match(file_name)

    if m is not None:
        n = m.group(1)
        if file_name == pre + n and int(n) <= file_cnt:
            return

    new_basename = pre + str(index) + ext.lower()
    new_file = os.path.join(path, new_basename)

    if os.path.exists(new_file):
        rename_if(pre, path, file, index + 1, file_cnt)
    else:
        old_file = os.path.join(path, os.path.basename(file))
        os.rename(old_file, new_file)
        print('rename:{} => {}'.format(old_file, new_file))


# 文件批量改名，自动编号从1开始
def rename(pre, paths):
    for path in paths:
        files = os.listdir(path)
        file_cnt = len(files)

        for file in files:
            rename_if(pre, path, file, 1, file_cnt)


# 获取文件md5
def get_file_md5(file_name):
    m = hashlib.md5()
    with open(file_name, 'rb') as f_obj:
        while True:
            data = f_obj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


# 根据文件md5识别重复文件，并将重复文件移到临时目录
def move_same_file(src_path, desc_path):
    files = os.listdir(src_path)
    file_dic = {}

    for file in files:
        full_path = os.path.join(src_path, file)
        if os.path.isdir(full_path):
            continue

        file_hash = get_file_md5(full_path)
        exist_file = file_dic.get(file_hash)

        if exist_file is not None:
            if exist_file != full_path:
                desc_file = os.path.join(desc_path, os.path.basename(file))
                os.rename(full_path, desc_file)
                print('found same:{} => {}'.format(full_path, desc_file))
        else:
            file_dic[file_hash] = full_path


def main():
    day_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    work_path = r'/Users/suqixu/Downloads'
    pre = '张恬语' + day_str + '_'
    v_path = os.path.join(work_path, 'v' + day_str)
    p_path = os.path.join(work_path, 'p' + day_str)
    t_path = os.path.join(work_path, 't' + day_str)

    mkdir_if([v_path, p_path, t_path])
    move_same_file(work_path, t_path)
    files = os.listdir(work_path)
    group(files, work_path, v_path, p_path)
    rename(pre, [v_path, p_path])
    print('done!')


if __name__ == '__main__':
    main()
