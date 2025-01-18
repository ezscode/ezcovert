#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   epub2html.py
@Time    :   2025-01-18 21:11:53
@Author  :   Ez
@Version :   1.0
@Desc    :   None

requirements: 

ebooklib==0.18
bs4==0.0.2

'''



import os
import sys 
import ebooklib 
from pathlib import Path
from bs4 import BeautifulSoup

def epub2htmls(file_path, save_dir=''):

    if len(save_dir.strip())==0:
        save_dir = Path(file_path).with_suffix("").as_posix()
    if not os.path.isdir(save_dir):os.makedirs(save_dir) 

    book = ebooklib.epub.read_epub(file_path)

    title = book.get_metadata('DC', 'title')
    creator = book.get_metadata('DC', 'creator')
    identifier = book.get_metadata('DC', 'identifier')

    print('-- title : ', title)
    print('-- creator : ', creator)
    print('-- identifier : ', identifier)

    items = book.get_items_of_type(ebooklib.ITEM_DOCUMENT) 

    idx = 0
    for item in items:
        idx += 1 
        name = item.get_name()
        print('-- ', idx, name)  

        content = item.get_body_content()
        # print(content)
        soup = BeautifulSoup(content, 'html.parser')

        # 漂亮地打印HTML
        pretty_html = soup.prettify()

        save_path = os.path.join(save_dir, f'{idx}.html') 
        with open(save_path, 'w') as f:
            f.write(name + '\n' + pretty_html)


def handle_paths(paths):
    for path in paths:  
        if os.path.isfile(path):    
            epub2htmls(path)
    


if __name__ == '__main__':
    
    paths = sys.argv[1:]
    print('-- ', paths)   
    handle_paths(paths) 

