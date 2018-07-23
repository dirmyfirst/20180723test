#coding:utf-8

import os


def get_file_name1(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''
    f_list = os.listdir(path)
    f_name = []
    for name in f_list:
        if os.path.splitext(name)[1] == '.py':
            f_name.append(os.path.join(path,name))
    return f_name

def get_file_name2():
    ''' 获取指定目录下的所有指定后缀的文件名 '''
    curdir = os.path.abspath(os.curdir)
    f_name = []
    for root, dirs, files in os.walk(curdir):
        for f_list in files:
            if os.path.splitext(f_list)[1] == '.py':
                f_name.append(os.path.join(root, f_list))
    return f_name
    

if __name__ == '__main__':

    path = 'F:\python学习\有用的小程序'
    get_file_name1(path)
