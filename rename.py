# -*- coding: utf-8 -*-

import os
import os.path
import datetime
import re


def mkdir_if(paths):
    for p in paths:
        if not os.path.exists(p):
            os.mkdir(p)


def move_by_ext(src_path, desc_path, file, ext_list):
    ext = os.path.splitext(file)[1]
    if ext.lower() in ext_list:
        src = os.path.join(src_path, os.path.basename(file))
        desc = os.path.join(desc_path, file)
        os.rename(src, desc)


def group(files, src_path, v_path, p_path):
    for file in files:
        move_by_ext(src_path, file, v_path, [".mp4"])
        move_by_ext(src_path, file, p_path, [".jpg", ".png"])


def rename_if(pre, path, file, index, file_cnt):
    file_name, ext = os.path.splitext(file)

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
        print("{} => {}".format(old_file, new_file))


def rename(pre, paths):
    for path in paths:
        files = os.listdir(path)
        file_cnt = len(files)

        for file in files:
            rename_if(pre, path, file, 1, file_cnt)


def run():
    day_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    work_path = r"E:\download\tmp"
    pre = "张恬语" + day_str + "_"
    v_path = os.path.join(work_path, "v" + day_str)
    p_path = os.path.join(work_path, "p" + day_str)
    paths = [v_path, p_path]

    mkdir_if(paths)
    files = os.listdir(work_path)
    group(files, work_path, v_path, p_path)
    rename(pre, paths)
    print("done!")


if __name__ == "__main__":
    run()
