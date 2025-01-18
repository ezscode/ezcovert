#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   docx2md.py
@Time    :   2025-01-18 11:46:17
@Author  :   Ez
@Version :   1.0
@Desc    :   None

***
requirements: 

mammoth==1.8.0
markdownify==0.13.1


'''



import os 
import sys 
import mammoth  
from markdownify import markdownify as md, ATX  


def docx2md(file_path):

    try:
        with open(file_path, "rb") as docx_file: 
            result = mammoth.convert_to_html(docx_file)
            html = result.value  
            # messages = result.messages 
            # with open(save_path, 'w') as f:f.write(html) 
            md_str = md(html, heading_style=ATX).strip()   
            return md_str
        
    except Exception as err:
        print('xx ', file_path, err) 



def handle_paths(paths):
    for path in paths:  
        if os.path.isfile(path):
            docx2md(path)
            
        if os.path.isdir(path):
            save_dir = path + '_md'
            if not os.path.isdir(save_dir):os.makedirs(save_dir) 
            for file_name in os.listdir(path):
                file_path = os.path.join(path, file_name)
                save_path = os.path.join(save_dir, file_name + '.md')
                if os.path.isfile(file_path):
                    docx2md(file_path, save_path) 

 
if __name__ == '__main__':
    
    paths = sys.argv[1:]
    print('-- ', paths)   
    handle_paths(paths) 
    
