#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pdf_split.py
@Time    :   2025-02-14 19:57:23
@Author  :   Ez
@Version :   1.0
@Desc    :   None


requirements: 

# pymupdf 中包含 fitz，如果单独安装 fitz，可能会遇到很多问题 
pymupdf==1.24.9 

'''


import os  
import sys 
import fitz 

def split_pdf(pdf_path, save_dir):
    if not pdf_path.lower().endswith('.pdf'): 
        return
    
    source_pdf = fitz.open(pdf_path)
    print('-- page num : ', source_pdf.page_count )
   
    # 遍历source_pdf中的每一页，page_number从0开始计数  
    for idx in range(source_pdf.page_count):
         
        output_pdf = fitz.open()    
   
        # 使用insert_pdf方法将源PDF文件的指定页面插入到新PDF文档中  
        output_pdf.insert_pdf(source_pdf, from_page=idx, to_page=idx)    
  
        save_path = os.path.join(save_dir, f'{idx}.pdf')
        print('-- ', save_path) 
    
        output_pdf.save(save_path)    
        output_pdf.close()    
         
    source_pdf.close()    



def handle_path(file_path):  
    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path) 
    save_dir = os.path.join(file_dir, os.path.splitext(file_name)[0])
    
    # if os.path.isdir(save_dir):
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir) 
    else:    
    #     print('xx 已存在文件夹，请检查') 
    #     return
        pass
    
    split_pdf(file_path, save_dir)
    
    


if __name__ == '__main__':
    
    file_path = sys.argv[1]
    print('-- ', file_path)   
    handle_path(file_path) 
    

