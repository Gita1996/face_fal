#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI,UploadFile,File
import ast
from tempfile import NamedTemporaryFile
from fastapi.concurrency import run_in_threadpool
import aiofiles
import asyncio
import os
import pandas as pd
from csv import DictReader
import ast
import csv
from ast import literal_eval
import remove_stop_words
from deepface import DeepFace
from deep_translator import GoogleTranslator
import preprocessing4
import fasttext_embedding
import remove_stop_words
from ast import literal_eval
import numpy as np
import ast
from tempfile import NamedTemporaryFile
from fastapi.concurrency import run_in_threadpool
import aiofiles
import asyncio
import os
import pandas as pd
from csv import DictReader
import ast
import csv
import remove_stop_words
import fasttext_embedding
import numpy as np
from numpy.linalg import norm
import numpy.random as npr
from random import randrange
from random import randint
import random
import sys
import os

app=FastAPI()
@app.post("/Hafez_fal/")
async def main(file: UploadFile = File(...), choice: str= 'interpretation' , num: int = 10):
    
    f=file.filename
    split= os.path.splitext(f)
  
    file_name = split[0]
    file_extension = split[1]
    file_extension=file_extension.lower()

    async with aiofiles.tempfile.NamedTemporaryFile("wb", delete=False,dir='.') as temp:
        try:
            contents = await file.read()
            await temp.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            await file.close()       
        

    t=temp.name
    d=pd.read_csv('falCsv_new.csv')
    a=d.faal_embedding
    r=list(a)
    faal2=list()
    for m in r:
        arr = [float(i) for i in m[1:-1].split(",")]
        faal2.append(arr)


    ####
    a=d.faal_embedding_chr
    r=list(a)
    faal_embedding_chr2=list()
    for m in r:
        arr = [float(i) for i in m[1:-1].split(",")]
        faal_embedding_chr2.append(arr)

    ###
    a=d.faal_embedding_wrd
    r=list(a)
    faal_embedding_wrd2=list()
    for m in r:
        arr = [float(i) for i in m[1:-1].split(",")]
        faal_embedding_wrd2.append(arr)

    ###
    a=d.interpretation_embedding
    r=list(a)
    maeni2=list()
    for m in r:
        arr = [float(i) for i in m[1:-1].split(",")]
        maeni2.append(arr)
    ###

    a=d.interpretation_embedding_chr
    r=list(a)
    maeni_embedding_chr2=list()
    for m in r:
        arr = [float(i) for i in m[1:-1].split(",")]
        maeni_embedding_chr2.append(arr)
    ###

    a=d.interpretation_embedding_wrd
    r=list(a)
    maeni_embedding_wrd2=list()
    for m in r:
        arr = [float(i) for i in m[1:-1].split(",")]
        maeni_embedding_wrd2.append(arr)
        
    similarities_maeni=list()
    similarities_faal=list()
    similarities_avg=list()
    similarities_sum=list()
    Top_values=list()
    dict_maeni=dict()
    dict_faal=dict()
    dict_avg=dict()
        
        

    try:
        if file_extension=='.jpg' or file_extension=='.jpeg' or file_extension=='.png':
            obj = DeepFace.analyze(img_path =t , actions = ['age', 'gender', 'race', 'emotion'])
            print(obj)
            dominant_emotion = obj['dominant_emotion']
            dominant_race = obj['dominant_race']
            gender=obj['gender']
            gender2=" "
            dominant_race2=" "
            dominant_emotion2=" "
            age=" "
            if gender=='Man':
                gender2='مرد'
            if gender=='Woman':
                gender2='زن'

            if dominant_race=='asian':
                dominant_race2='ایران'
            if dominant_race=='indian':
                dominant_race2='هند'
            if dominant_race=='black':
                dominant_race2='سیاه' 
            if dominant_race=='white':
                dominant_race2='سفید' 
            if dominant_race=='middle eastern':
                dominant_race2='شرقی' 
            #'latino hispanic'
            if dominant_race=='latino hispanic':
                dominant_race2='یونان' 



            if dominant_emotion=='angry':
                dominant_emotion2='خشمگین'
            if dominant_emotion=='disgust':
                dominant_emotion2='نفرت انگیز'
            if dominant_emotion=='fear':
                dominant_emotion2='ترس'
            if dominant_emotion=='happy':
                dominant_emotion2='شاد'
            if dominant_emotion=='sad':
                dominant_emotion2='غمگین'
            if dominant_emotion=='surprise':
                dominant_emotion2='شگفت'
            if dominant_emotion=='neutral':
                dominant_emotion2='عادی' 

            if obj['age']<=10:
                age='بچه'
            if obj['age']>10 and obj['age']<20:
                age='نوجوان'
            if 20<=obj['age'] and obj['age']<45:
                age='جوان'
            if obj['age']>=45 and obj['age']<70:
                age='میان سال'
            if obj['age']>=70:
                age='پیر'
                
            if (age=='بچه' or age=='نوجوان') and gender=='Woman':
                gender2='دختر'

            if (age=='بچه' or age=='نوجوان') and gender=='man':
                gender2='پسر'
            
            
            txt="{0} {1} {2} {3} ".format(gender2, age, dominant_emotion2 , dominant_race2)
            d=pd.read_csv('falCsv_new.csv')
            s=remove_stop_words.remove_stop_words(txt)
            s1=preprocessing4.clean_text2(s)
            n=fasttext_embedding.build_embedding_matrix_chr(s1)

            b=np.array(n)


            i=0
            for e in maeni_embedding_chr2:
                a=np.array(e)
                cosine = np.dot(a,b)/(norm(a)*norm(b))
                similarities_maeni.append(cosine)
                dict_maeni[i]=cosine
                i=i+1

            i=0
            for e in faal_embedding_chr2:
                a=np.array(e)
                cosine = np.dot(a,b)/(norm(a)*norm(b))
                similarities_faal.append(cosine) 
                dict_faal[i]=cosine
                i=i+1

            for i in range(len(faal_embedding_chr2)):
                a=(similarities_maeni[i]+similarities_faal[i])/2
                similarities_avg.append(a)
                dict_avg[i]=a



            def roulette_wheel_selection1(similarities, num):
                similarities3=list()
                similarities=np.array(similarities)
                top_poems=sorted(range(len(similarities)), key = lambda sub: similarities[sub])[-num:]
                for a in top_poems:
                    similarities3.append(similarities[a])
                print(similarities3)
                indexes=list()
                current_sum=0
                for i in range(len(similarities3)):
                    current_sum+=similarities3[i]
                    similarities_sum.append(current_sum)
                rand_sum=random.uniform(1, similarities_sum[num-1])
                rand_index=0
                for i in range(num-1):
                    if rand_sum>similarities_sum[i] and rand_sum<=similarities_sum[i+1]:
                        rand_index=i+1
                return np.array(top_poems)[rand_index]


            def select_poem(choice, num):
                if choice=='poem':
                    a=roulette_wheel_selection1(similarities_faal, num)
                    return d['faal'][a].replace('\\r\\n', '   '),d['interpretation'][a]
                if choice=='interpretation':
                    a=roulette_wheel_selection1(similarities_maeni, num)
                    return d['faal'][a].replace('\\r\\n', '   '),d['interpretation'][a]
                if choice=='both':
                    a=roulette_wheel_selection1(similarities_avg, num)
                    return d['faal'][a].replace('\\r\\n', '   '),d['interpretation'][a]

            def roulette_wheel_selection(population):   
                population_fitness = sum(s for s in population)       
                chromosome_probabilities = [s/population_fitness for s in population]    
                r=npr.choice(len(population), p=chromosome_probabilities)
                r2=d['interpretation'][r]
                return r2

            x,y=select_poem(choice, num)
            return {'poem':str(x), 'interpretation':str(y)}
        else:
            msg="not proper file"
            return msg
    except:
        msg2="not face detected"
        return msg2








