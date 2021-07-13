import matplotlib.pyplot as plt
import wordcloud
import jieba
import random
from imageio import imread
import requests
from bs4 import BeautifulSoup
global_text = ""
def getDetail(data):
    global global_text
    data = BeautifulSoup(data,"html.parser")
    spans = data.find_all(class_="short")
    for i in spans:
        global_text += ",".join(jieba.cut(str(i.text).strip())) # 对获取到的热评分词
def toWordCloud():
    global global_text
    fonts = glob.glob('Users\Administrator\PycharmProjects\juexingniandai\lycc\ziti\*.ttf')
    font = random.choice(fonts)
    print(font)
    color_masks = glob.glob('/Users/zhubowen/Desktop/Web-Crawler/online_word_cloud/pict/*.jpg')
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
    wcd.generate(global_text)
    plt.imshow(wcd)
    wcd.to_file("ciyuntu.jpg")
    plt.axis('off')
    plt.show()
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"
    }
    url = 'https://movie.douban.com/subject/30228394/comments?percent_type=h&start={}&limit=20&status=P&sort=new_score'
    for i in range(random.randint(1,30)):
        new_url = url.format(i * 20)
        response = requests.get(url=url,headers=headers)
        response.encoding = 'utf-8'
        getDetail(response.text)
    toWordCloud()