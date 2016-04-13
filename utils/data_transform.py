# -*- coding: utf-8 -*-
import jieba
import data_clean
import os

_stop_words_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stop_dict/stopwords.txt")


def load_stop_words(filename=_stop_words_filename):
    stopwords = {}
    with open(filename, "rb") as f:
        for line in f:
            word = line.strip()
            if word:
                stopwords[word] = 1
    stopwords[" "] = 1
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

