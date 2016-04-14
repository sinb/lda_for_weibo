# -*- coding: utf-8 -*-
import jieba
import data_clean
import os
import logging
import numpy as np

logger = logging.getLogger('lda_for_weibo')
_stop_words_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stop_dict/stopwords.txt")


def _isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def load_stop_words(filename=_stop_words_filename):
    stopwords = {}
    with open(filename, "rb") as f:
        for line in f:
            word = line.strip()
            if word:
                stopwords[word.decode('utf-8')] = 1
    stopwords[u" "] = 1
    return stopwords


def build_word_set(filename, stop_words_filename=None):
    if stop_words_filename is None:
        stop_words = load_stop_words()
    else:
        stop_words = load_stop_words(stop_words_filename)

    word_set = {}
    with open(filename, 'rb') as f:
        for line in f:
            words = jieba.cut(data_clean.clean(line), cut_all=False)
            for word in words:
                if stop_words.get(word, 0):
                    continue
                else:
                    word_set[word] = word_set.get(word, 1)
    return word_set


def truncate_word_set(word_dic):
    word_lst = word_dic.keys()
    word_lst.sort(key=lambda x: len(x))
    word_lst_copy = word_lst[:]
    for i in word_lst:
        if i.encode('utf-8').isalnum() or _isfloat(i):
            word_lst_copy.remove(i)
    return word_lst_copy


def build_n_truncate(filename, stop_words_filename=None):
    import time
    start_time = time.time()
    word_set_dic = build_word_set(filename, stop_words_filename)
    word_set = truncate_word_set(word_set_dic)
    elapsed_time = time.time() - start_time
    logger.info("build word set cost {} time".format(elapsed_time))
    return word_set


def build_lda_for_data(filename, word_set):
    word_set_dic = dict(zip(word_set, range(0, len(word_set))))
    dataset = []
    with open(filename, 'rb') as f:
        for line in f:
            one_data = np.zeros(len(word_set), dtype=int)
            words = jieba.cut(data_clean.clean(line), cut_all=False)
            for word in words:
                idx = word_set_dic.get(word, -1)
                if idx < 0:
                    continue
                else:
                    one_data[idx] += 1
            dataset.append(one_data)
    return np.array(dataset), word_set_dic


def load_raw_data(filename):
    raw_dataset = []
    with open(filename, 'rb') as f:
        for line in f:
            raw_dataset.append(data_clean.clean(line))
    return raw_dataset
