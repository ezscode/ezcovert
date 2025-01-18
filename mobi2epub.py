#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mobi2epub.py
@Time    :   2025-01-18 21:11:33
@Author  :   Ez
@Version :   1.0
@Desc    :   None



这里使用 calibre 的 ebook-convert 命令进行转换 
详见：https://manual.calibre-ebook.com/zh_CN/generated/zh_CN/ebook-convert.html 

Linux 安装 calibre : sudo apt install calibre 
macOS 安装 calibre : brew install calibre   


'''


import sys
import os
import subprocess


def mobi2epub(file_path, save_path=''):
    
    try:
        if not file_path.ends("azw3")  and not file_path.ends("mobi"):return

        if len(save_path.strip()) == 0:
            if file_path.ends("azw3"):
                save_path = file_path.replace('.azw3', '.epub')
            elif file_path.ends("mobi"):
                save_path = file_path.replace('.mobi', '.epub') 
        
        commands = []
        commands.append("ebook-convert")
        commands.append(file_path)
        commands.append(save_path)

        subprocess.call(commands)

    except Exception as err:
        print('xx ', file_path, err)  




def handle_paths(paths):
    for path in paths:  
        if os.path.isfile(path):
            mobi2epub(path)
            
        if os.path.isdir(path):  
            for file_name in os.listdir(path):
                file_path = os.path.join(path, file_name) 
                if os.path.isfile(file_path):
                    mobi2epub(file_path) 



if __name__ == '__main__':
    
    paths = sys.argv[1:]
    if len(paths) == 0: # 处理当前目录下的文件 
        paths = [os.getcwd()] 

    print('-- ', paths)   
    handle_paths(paths) 
    
    
