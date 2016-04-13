# -*- coding: utf-8 -*-
from utils import data_clean, data_transform
import jieba

def print_file(name):
    import os
    name = os.path.join(os.path.dirname(os.path.realpath(__file__)), name)
    try:
        with open(name, 'rb') as f:
            for line in f:
                words = jieba.cut(data_clean.clean(line), cut_all=False)
                print "|".join(words)
    except IOError as e:
        print e.filename + " not found"
        print os.path.isfile(e.filename)

filename = 'data/3000_weibo.txt'
print_file(filename)
