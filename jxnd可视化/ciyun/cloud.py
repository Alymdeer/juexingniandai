import glob
import random
import imageio
import wordcloud
import matplotlib.pyplot as plt
import pandas as pd
import os

data = pd.read_csv(r'C:\Users\86136\Desktop\ciyun2\bili_danmu2(1).csv', encoding='utf-8')
with open(r'C:\Users\86136\Desktop\ciyun2\bili.txt', 'a+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0]) + '\t' + str(line[1]) + '\n'))


def toWordCloud():
    with open(r'C:\Users\86136\Desktop\ciyun2\bili.txt', encoding='utf-8', errors='ignore') as f:
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