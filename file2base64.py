#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file2base64.py
@Time    :   2025-01-18 12:01:48
@Author  :   Ez
@Version :   1.0
@Desc    :   None


'''

import os
import sys 
import base64

 
def base642file(base64_str, save_path): 
    bytes = base64.b64decode(base64_str.encode('utf-8'))
    with open(save_path, 'wb') as f:f.write(bytes) 

def file2base64(file_path):

    bytes = open(file_path, 'rb').read()  
    base64_str = base64.b64encode(bytes).decode('utf-8') 
    return base64_str




if __name__ == '__main__':
    
    path = sys.argv[1]
    print('-- ', path) 
    base64_str = file2base64(path)

    
    