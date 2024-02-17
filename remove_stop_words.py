#!/usr/bin/env python
# coding: utf-8

# In[53]:


import re
import preprocessing4


def remove_stop_words(text):
    file='stop_words.txt'
    a=list()
    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            x=line.split()
            a.append(x[0])
    t1=text.split('\n')
    c=list()
    for v in t1:
        t=v.split()
        for m in t:
            for r in a:
    #        print(r)
                if(m==r):
                    m=re.sub(r, '', m)
            c.append(m)
        c.append('\n')

    text_new=""
    for r in c:
        text_new+=" "+str(r)
    text_new=re.sub(r" +", " ",text_new)

    return text_new




