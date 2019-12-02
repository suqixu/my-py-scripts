# -*- coding: utf-8 -*-
# author : zhangzaiyuan
# date : 20191202
# email : suqixu@126.com
#
# 脚本功能:
# 1、解析chrome书签并导出html文件

import json
import os

title_stack = []
url_buffer = []


# 解析书签文件夹
def parse_folder(item, data):
    if item['type'] == 'folder':
        title_stack.append(item['name'])

        found_url = False
        children_item_list = item['children']

        for children_item in children_item_list:
            children_type = children_item['type']
            if children_type == 'url':
                found_url = True
                url_buffer.append('<a href="{}" target="_blank">{}</a><br/>\n'
                                  .format(children_item['url'], children_item['name']))
            elif children_type == 'folder':
                parse_folder(children_item, data)

        if found_url:
            data.append('<h4>{}({})</h4>\n'.format(' >> '.join(title_stack), len(url_buffer)))
            data.append(''.join(url_buffer))
            url_buffer.clear()

        title_stack.pop()


# 输出html头部及样式
def append_html_head(data):
    html_head = """
    <head>
        <title>书签</title>
        <style>
            body, div,input,a{ font-size: 16px; }
            a {text-decoration: none;}
            a:visited {color:#004d00} /* 已访问的链接 */
            a:hover {text-decoration: none;color: #c00;} /* 当有鼠标悬停在链接上 */
            a:active {color: #f00} /* 被选择的链接 */
        </style>
    </head>
    <body> 
        """
    data.append(html_head)


# 解析书签文件
def parse(data):
    bookmarks_name = r'{}\AppData\Local\Google\Chrome\User Data\Default\Bookmarks'\
        .format(os.path.expanduser('~'))
    if not os.path.exists(bookmarks_name):
        return False

    in_bookmark_file = open(bookmarks_name, 'r', encoding="UTF-8")
    json_object = json.load(in_bookmark_file)
    bookmark_root = json_object['roots']['bookmark_bar']['children']

    for item in bookmark_root:
        title_stack.clear()
        parse_folder(item, data)

    in_bookmark_file.close()
    data.append("</body>")
    return True


# 导出html文件
def export(file_name, data):
    out_bookmark_file = open(file_name, 'w', encoding='UTF-8')
    out_bookmark_file.write(''.join(data))
    out_bookmark_file.close()


def main():
    html = []
    append_html_head(html)
    if not parse(html):
        print('export failed!')
    else:
        export('my_bookmarks.html', html)
        print('export success!')


if __name__ == '__main__':
    main()