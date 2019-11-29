# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191129
# email : suqixu@126.com
#
# 脚本功能:
# 1、剪贴板增强

import shelve
import pyperclip

indicator = ">>> "
usage = """
用例: [save <args>] [args] [list] [view <args>] [exit]
      save <args>  保存系统剪贴板内容到缓存
      <arg>       复制缓存内容到系统剪贴板
      list        查看当前缓存列表
      view <args> 查看缓存内容
      del <args>  删除缓存内容
      help        说明
      exit        退出
"""
cmd_list = ['save', 'list', 'view', 'del', 'help', 'exit']


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
            print('arg invalid, can not is ' + str(cmd_list))
        else:
            copy_db[arg] = pyperclip.paste()
            print('[{}] => save complete'.format(arg))


# 查看缓存
def view_cmd(args, copy_db):
    if len(args) < 2:
        print('view arg invalid')
    else:
        for arg in args[1:]:
            arg = arg.lower()
            try:
                text = copy_db[arg]
                if text is not None:
                    line = '-' * 10
                    print('[{}]\n{}\n{}\n{}'.format(arg, line, text, line))
                else:
                    print('[{}] => is empty'.format(arg))
            except KeyError:
                print('[{}] => is not exist'.format(arg))


# 删除缓存
def del_cmd(args, copy_db):
    if len(args) < 2:
        print('del arg invalid')
    else:
        deled_list = []
        for arg in args[1:]:
            arg = arg.lower()
            try:
                del copy_db[arg]
                deled_list.append(arg)
            except KeyError:
                print('[{}] => is not exist'.format(arg))

        print('{} => del complete'.format(str(deled_list)))


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
    try:
        copy_db = shelve.open('.copy.db')
        cmd, args = parse_cmd(usage + indicator)

        while cmd != 'exit':
            if cmd == 'save':
                save_cmd(args, copy_db)
            elif cmd == 'view':
                view_cmd(args, copy_db)
            elif cmd == 'list':
                list_cmd(copy_db)
            elif cmd == 'del':
                del_cmd(args, copy_db)
            elif cmd == 'help':
                print(usage, end='')
            else:
                default_cmd(cmd, copy_db)

            cmd, args = parse_cmd(indicator)

    finally:
        copy_db.close()


if __name__ == '__main__':
    main()
