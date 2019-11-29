# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191129
# email : suqixu@126.com
#
# 脚本功能:
# 1、剪贴板增强

import sys
import pyperclip
import shelve

indicator = ">>> "
usage = """
用例: [save <key>] [key] [list] [view <key>] [exit]
      save <key>  保存系统剪贴板内容到缓存
      <key>       复制缓存内容到系统剪贴板
      list        查看当前缓存列表
      view <key>  查看缓存内容
      help        说明
      exit        退出
"""
cmd_list = ['save', 'list', 'view', 'help', 'exit']


# 解析命令和参数
def parse_cmd(text):
    input_cmd = input(text)
    args = input_cmd.split()
    cmd = args[0].lower()
    return cmd, args


# 保存剪贴板到缓存
def save_cmd(args, copy_db):
    if len(args) < 2:
        print('save arg invalid')
    else:
        arg = args[1].lower()
        if arg in cmd_list:
            print('key name invalid, can not is ' + str(cmd_list))
        else:
            copy_db[arg] = pyperclip.paste()
            print('save complete')


# 查看缓存
def view_cmd(args, copy_db):
    if len(args) < 2:
        print('view arg invalid')
    else:
        arg = args[1].lower()
        if arg in cmd_list:
            print('key name invalid, can not is ' + str(cmd_list))
        else:
            try:
                text = copy_db[arg]
                if text is not None:
                    print(text)
                else:
                    print('the key is empty')
            except KeyError as e:
                print('the key is not exist')


# 查看缓存列表
def list_cmd(copy_db):
    keys = list(copy_db.keys())
    print(str(keys))


# 其他命令
def default_cmd(cmd, copy_db):
    keys = list(copy_db.keys())
    if cmd in keys:
        pyperclip.copy(copy_db[cmd])
        print('copy complete')
    else:
        print('command not found')


def main():
    copy_db = shelve.open('.copy.db')
    cmd, args = parse_cmd(usage + indicator)

    while cmd != 'exit':
        if cmd == 'save':
            save_cmd(args, copy_db)
        elif cmd == 'view':
            view_cmd(args, copy_db)
        elif cmd == 'list':
            list_cmd(copy_db)
        elif cmd == 'help':
            print(usage, end='')
        else:
            default_cmd(cmd, copy_db)

        cmd, args = parse_cmd(indicator)


if __name__ == '__main__':
    main()
