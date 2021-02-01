# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import random

'''
import text file
'''

def create_dct(txt, is_lenin):
    lst = []
    nlst =[]
    f = open(txt)
    lines = list(f.readlines())
    f.close()
    
    '''
    clean lines
    '''
    for line in lines:
        if line != '\n': 
            line = line[:-1]
            lst.append(line)
    
    for item in lst:
        dct = {}
        dct['statement'] = item
        dct['is_lenin'] = is_lenin
        nlst.append(dct)
    
    return nlst

data = create_dct('is_lenin', 1)
data += create_dct('not_lenin', 0)

random.shuffle(data)

with open('lenin_dataset.json', 'w') as outfile:
    json.dump(data, outfile)
