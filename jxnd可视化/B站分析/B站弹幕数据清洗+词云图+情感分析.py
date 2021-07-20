#!/usr/bin/env python
# coding: utf-8

# In[24]:


import glob
import random
import imageio
import wordcloud
import matplotlib.pyplot as plt
import pandas as pd
import os


# In[25]:


data = pd.read_csv(r'C:\Users\86136\Desktop\ciyun2\bili_danmu2(1).csv', encoding='utf-8')


# In[26]:


data.isnull().sum()


# In[27]:


data.dtypes


# In[28]:


#文本内容清洗，去除表达符号、特殊字符等等
import re
pattern = r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_^{|}~—！，。？、￥…（）：【】《》‘’“”\s]+" 
re_obj = re.compile(pattern)

def clear(text):
    return re_obj.sub("",text)

data.comments = data.comments.apply(clear)



# In[29]:


bool=data.comments!=''
bool.sum()
data2=data[bool]
data2


# In[30]:


with open(r'C:\Users\86136\Desktop\ciyun2\bilibili.txt','a+', encoding='utf-8') as f:
    for line in data2.values:
        f.write((str(line[0])+'\t'+str(line[1])+'\n'))


# In[32]:


#分词
import jieba
def cut_word(text):
    return jieba.cut(text)
data2.comments=data2.comments.apply(cut_word)


# In[39]:


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
data2.comments= data2.comments.apply(remove_stopword)
#data2.comments[134]


# In[92]:


d3= list ( filter ( None,data2.comments))
d4=[]
for i in d3:
    x="".join(i)
    d4.append(x)
d4


# In[81]:


with open(r'C:\Users\86136\Desktop\ciyun2\bilibilibili.txt','w',encoding='utf-8') as f:
       for li in d4:
            f.write(li+"\n")


# In[83]:


def toWordCloud():

    with open(r'C:\Users\86136\Desktop\ciyun2\bilibili.txt', encoding='utf-8', errors='ignore') as f:
        data = f.read()
    f.close()
    fonts = glob.glob(r'C:\Users\86136\Desktop\ciyun2\ziti\*.ttf')
    font = random.choice(fonts)
    color_masks = glob.glob(r'C:\Users\86136\Desktop\ciyun2\*.JPG')
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
    wcd.to_file("ciyuntu_bili.png")
    plt.axis('off')
    plt.show()
if __name__ == '__main__':
    toWordCloud()


# In[86]:


def toWordCloud():

    with open(r'C:\Users\86136\Desktop\ciyun2\bilibilibili.txt', encoding='utf-8', errors='ignore') as f:
        data = f.read()
    f.close()
    fonts = glob.glob(r'C:\Users\86136\Desktop\ciyun2\ziti\*.ttf')
    font = random.choice(fonts)
    color_masks = glob.glob(r'C:\Users\86136\Desktop\ciyun2\*.JPG')
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
    wcd.to_file("ciyuntu.png")
    plt.axis('off')
    plt.show()
if __name__ == '__main__':
    toWordCloud()


# In[23]:


from snownlp import SnowNLP
import codecs
import os
import pandas as pd


# In[87]:


#情感各分数段出现频率以及可视化
source = open(r'C:\Users\86136\Desktop\ciyun2\bilibilibili.txt', "r", encoding='utf-8')
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


# In[90]:


#情感变化及可视化
from snownlp import SnowNLP
import codecs
import os

source = open(r'C:\Users\86136\Desktop\ciyun2\bilibilibili.txt',"r", encoding='utf-8')
line = source.readlines()
sentimentslist = []
for i in line:
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(0, 3426, 1), sentimentslist, 'r-')
plt.xlabel('Number')
plt.ylabel('Sentiment')
plt.title('Analysis of Sentiments')
plt.show()


# In[ ]:




