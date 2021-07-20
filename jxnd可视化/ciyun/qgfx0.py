# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import os
import pandas as pd

#将爬取弹幕得到的csv文件转化为txt文件并保存
data = pd.read_csv(r'C:\Users\86136\Desktop\ciyun2\bili_danmu2(1).csv', encoding='utf-8')
with open(r'C:\Users\86136\Desktop\ciyun2\bili.txt','a+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0])+'\t'+str(line[1])+'\n'))

#情感各分数段出现频率以及可视化
source = open(r'C:\Users\86136\Desktop\ciyun2\bili.txt', "r", encoding='utf-8')
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
