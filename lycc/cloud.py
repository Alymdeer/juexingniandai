import glob
import random
import imageio
import wordcloud
import matplotlib.pyplot as plt
def toWordCloud():
    with open( 'TF-IDFanalyse.txt','r') as f:
        data=f.read()
    f.close()
    fonts = glob.glob(r'\Users\Administrator\PycharmProjects\juexingniandai\lycc\ziti\*.ttf')
    font = random.choice(fonts)
    color_masks = glob.glob(r'\Users\Administrator\PycharmProjects\juexingniandai\main-1\ciyun\*.jpg')
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