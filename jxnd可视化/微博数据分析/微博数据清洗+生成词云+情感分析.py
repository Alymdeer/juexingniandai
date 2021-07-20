#!/usr/bin/env python
# coding: utf-8

# In[1]:


import glob
import random
import imageio
import wordcloud
import matplotlib.pyplot as plt
import pandas as pd
import os


# In[16]:


data = pd.read_excel(r'C:\Users\86136\Desktop\ciyun2\#觉醒年代#.xlsx', encoding='utf-8')


# In[17]:


data.drop('username',axis = 1,inplace = True)
data1=data


# In[4]:


data.isnull().sum()


# In[5]:


data.dtypes


# In[6]:


#说明每一条评论基本都是有文字的，文本内容清洗之后数目保持不变
bool=data.comment!=''
bool.sum()


# In[7]:



with open(r'C:\Users\86136\Desktop\ciyun2\weibo.txt','a+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0])+'\t'+str(line[1])+'\n'))


# In[8]:


#分词
import jieba
def cut_word(text):
    return jieba.cut(text)
data.comment=data.comment.apply(cut_word)


# In[9]:


#停用词处理
def get_stopword():
    s = set()
    with open(r'C:\Users\86136\Desktop\ciyun2\StopWords.txt',encoding = 'UTF-8') as f:
        for line in f:
            s.add(line.strip())
    return s

def remove_stopword(words):
    return [word for word in words if word not in stopword]

stopword = get_stopword()
data.comment= data.comment.apply(remove_stopword)
data.comment


# In[10]:


#将lisi里的list转化为str
d3= list ( filter ( None,data.comment))
d4=[]
for i in d3:
    x="".join(i)
    d4.append(x)
d4


# In[11]:


#生成.txt文件，用于词云图
with open(r'C:\Users\86136\Desktop\ciyun2\weibo2.txt','w',encoding='utf-8') as f:
        for li in d4:
             f.write(li+"\n")


# In[12]:


def toWordCloud():

    with open(r'C:\Users\86136\Desktop\ciyun2\weibo2.txt', encoding='utf-8', errors='ignore') as f:
        data = f.read()
    f.close()
    fonts = glob.glob(r'C:\Users\86136\Desktop\ciyun2\ziti\*.ttf')
    font = random.choice(fonts)
    color_masks = glob.glob(r'C:\Users\86136\Desktop\ciyun2\25.JPG')
    color_mask = random.choice(color_masks)
    color_mask = imageio.imread(color_mask)
    wcd = wordcloud.WordCloud(
        font_path=font,  # 设置字体
        background_color="white",  # 背景颜色
        max_words=200,  # 词云显示的最大词数
        mask=color_mask,  # 设置背景图片
        max_font_size=150,  # 字体最大值
        mode="RGBA",
        width=500,
        height=400,
        collocations=False
    )
    wcd.generate(data)
    plt.imshow(wcd)
    wcd.to_file("ciyuntu_weibo.png")
    plt.axis('off')
    plt.show()
if __name__ == '__main__':
    toWordCloud()


# In[13]:


from snownlp import SnowNLP
import codecs
import os
import pandas as pd


# In[18]:


#文本内容清洗，去除表达符号、特殊字符等等
import re
pattern = r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_^{|}~—！，。？、￥…（）：【】《》‘’“”\s]+" 
re_obj = re.compile(pattern)

def clear(text):
    return re_obj.sub("",text)

data1.comment=data1.comment.apply(clear)


# In[21]:


#停用词处理
def get_stopword():
    s = set()
    with open(r'C:\Users\86136\Desktop\ciyun2\StopWords.txt',encoding = 'UTF-8') as f:
        for line in f:
            s.add(line.strip())
    return s

def remove_stopword(words):
    return [word for word in words if word not in stopword]

stopword = get_stopword()
data1.comment= data1.comment.apply(remove_stopword)


# In[23]:


d3= list ( filter ( None,data1.comment))
d4=[]
for i in d3:
    x="".join(i)
    d4.append(x)
d4


# In[24]:


#生成.txt文件，用于情感分析
with open(r'C:\Users\86136\Desktop\ciyun2\weibo3.txt','w',encoding='utf-8') as f:
        for li in d4:
             f.write(li+"\n")


# In[25]:


#情感各分数段出现频率以及可视化
source = open(r'C:\Users\86136\Desktop\ciyun2\weibo3.txt', "r", encoding='utf-8')
line = source.readlines()
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

import matplotlib.pyplot as plt
import numpy as np
plt.hist(sentimentslist, bins = np.arange(0, 1, 0.01), facecolor = 'r')
plt.xlabel('Sentiments Probability')
plt.ylabel('Quantity')
plt.title('Analysis of Sentiments')
plt.show()


# In[27]:


#情感变化及可视化
from snownlp import SnowNLP
import codecs
import os

source = open(r'C:\Users\86136\Desktop\ciyun2\weibo3.txt',"r", encoding='utf-8')
line = source.readlines()
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(0, 989, 1), sentimentslist, 'r-')
plt.xlabel('Number')
plt.ylabel('Sentiment')
plt.title('Analysis of Sentiments')
plt.show()


# In[ ]:




