# -*- coding: utf-8 -*-
_stop_words_filename = "../data/stopwords.txt"


def load_stop_words(filename=_stop_words_filename):
    """
    从文件读取停用词, 保存成词典
    空格也是停用词
    :param filename:
    :return:
    """
    stopwords = {}
    with open(filename, "rb") as f:
        for line in f:
            word = line.strip()
            if word:
                stopwords[word] = 1
    stopwords[" "] = 1
    return stopwords
