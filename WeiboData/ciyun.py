import glob
import random
import imageio
import wordcloud
import matplotlib.pyplot as plt
import pandas as pd
import os
data = pd.read_excel(r'D:\juexingniandai\#周恩来#.xlsx', encoding='utf-8')
bool=data.comment.notnull()
data2=data[bool]
#分词
import jieba
def cut_word(text):
    return jieba.cut(text)
data2.comment=data2.comment.apply(cut_word)
#停用词处理
def get_stopword():
    s = set()
    with open(r'D:\juexingniandai\StopWords.txt',encoding = 'UTF-8') as f:
        for line in f:
            s.add(line.strip())
    return s

def remove_stopword(words):
    return [word for word in words if word not in stopword]

stopword = get_stopword()
data2.comment= data2.comment.apply(remove_stopword)
data2.comment
#将lisi里的list转化为str
d3= list ( filter ( None,data2.comment))
d4=[]
for i in d3:
    x="".join(i)
    d4.append(x)
#生成.txt文件，用于词云图
with open(r'D:\juexingniandai\周恩来.txt','w',encoding='utf-8') as f:
        for li in d4:
             f.write(li+"\n")
def toWordCloud():

    with open(r'D:\juexingniandai\周恩来.txt', encoding='utf-8', errors='ignore') as f:
        data = f.read()
    f.close()
    fonts = glob.glob(r'D:\juexingniandai\字体\*.ttf')
    font = random.choice(fonts)
    color_masks = glob.glob(r'D:\juexingniandai\树.JPG')
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