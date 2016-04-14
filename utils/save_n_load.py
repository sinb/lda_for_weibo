# -*- coding: utf-8 -*-
import numpy as np
import logging
import os

logger = logging.getLogger('lda_for_weibo')
logger.setLevel(logging.INFO)


def save_word_set(word_set, filename):
    word_set = np.asarray(word_set)
    np.save(open(filename, 'wb'), word_set)
    logger.info("save word set to {} done".format(filename))


def load_word_set(filename):
    return np.load(open(filename, 'rb'))


def save_by_class(model, raw_dataset, dir):
    doc_topic = model.doc_topic_
    weibo_cls = {}
    for i in range(0, len(raw_dataset)):
        topic_id = doc_topic[i].argmax()
        weibo_cls[topic_id] = weibo_cls.get(topic_id, [])
        weibo_cls[topic_id].append(raw_dataset[i])
    for k, v in weibo_cls.items():
        with open(os.path.join(dir, str(k)+'.txt'), 'wb') as f:
            for weibo in v:
                f.write(weibo)
