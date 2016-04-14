# -*- coding: utf-8 -*-
from utils import data_clean, data_transform, save_n_load
import lda
import numpy as np

weibo_filename = 'data/3000_weibo.txt'
word_set_filename = 'data/word_set.npy'

word_set = data_transform.build_n_truncate(weibo_filename)
save_n_load.save_word_set(word_set, "data/word_set.npy")
word_set = save_n_load.load_word_set(word_set_filename)
raw_dataset = data_transform.load_raw_data(weibo_filename)

X, word_set_dic = data_transform.build_lda_for_data(weibo_filename, word_set)
id_word_dic = dict([(v, k) for k, v in word_set_dic.items()])

model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)

n_top_words = 20
topic_word = model.topic_word_
# 显示每个话题下最可能出现的词语
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(word_set)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    topic_words = [word.encode('utf-8') for word in topic_words]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))

# 按照话题将微博分类,保存在'data/classes'
save_n_load.save_by_class(model, raw_dataset, 'data/classes')