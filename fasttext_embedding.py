#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
EMB_PATHS = ['poem3_model3_new_chr.vec',
             'poem3_model3_new_wrd.vec']

EMB_SIZE = 100
MAX_LEN = 1000

def get_coefs(word, *arr):
    return word, np.asarray(arr, dtype='float32')

embedding_path_chr = EMB_PATHS[0]
embedding_index_chr = dict(get_coefs(*o.strip().split(" ")) for o in open(embedding_path_chr, encoding="utf8"))

def build_embedding_matrix_chr(word_index):
    embedding_matrix = np.zeros(EMB_SIZE)
    for word in word_index.split(' '):
        embedding_vector = embedding_index_chr.get(word)
        if embedding_vector is not None:
            embedding_matrix = embedding_matrix + embedding_vector
    embedding_matrix = embedding_matrix/len(word_index)
    return embedding_matrix


embedding_path_wchr = EMB_PATHS[1]
embedding_index_wchr = dict(get_coefs(*o.strip().split(" ")) for o in open(embedding_path_wchr, encoding="utf8"))

def build_embedding_matrix_wchr(word_index):
    embedding_matrix = np.zeros(EMB_SIZE)
    for word in word_index.split(' '):
        embedding_vector = embedding_index_wchr.get(word)
        if embedding_vector is not None:
            embedding_matrix = embedding_matrix + embedding_vector
    embedding_matrix = embedding_matrix/len(word_index)
    return embedding_matrix

def sentence_embedding(word_index):
    v1=build_embedding_matrix_chr(word_index)
    v2=build_embedding_matrix_wchr(word_index)
    v3=np.concatenate((v1,v2))
    return v3






