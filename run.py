# -*- coding: utf-8 -*-
from utils import data_clean, data_transform
import jieba
import os


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


def truncate_word_set(word_dic):
    word_lst = word_dic.keys()
    word_lst.sort(key=lambda x: len(x))
    for i in word_lst:
        i = i.encode('utf-8')
        if i.isalnum():
            word_lst.remove(i)
    return word_lst

weibo_filename = 'data/3000_weibo.txt'
word_set = data_transform.build_word_set(weibo_filename)

word_set = truncate_word_set(word_set)
for i in word_set:
    print i

# for i in word_set.keys():
#     i = i.encode('utf-8')
#     if i.isalnum():
#         continue
#     else:
#         try:
#             float(i)
#         except ValueError:
#             print i
#
