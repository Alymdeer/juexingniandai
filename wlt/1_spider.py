import requests
from lxml import etree
import time
import random
import csv
import pandas as pd

def get_target(keyword, page,saveName):
    result = pd.DataFrame()

    for i in range(1, page + 1):
        headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'}

        url = 'https://search.bilibili.com/all?keyword={}&from_source=nav_suggest_new0&page={}'.format(keyword, i)
        html = requests.get(url.format(i), headers=headers)
        bs = etree.HTML(html.text)
        items = bs.xpath('//li[@class = "video-item matrix"]')
        for item in items:
            video_url = item.xpath('div[@class = "info"]/div/a/@href')[0].replace("//","")                   #每个视频的来源地址
            title = item.xpath('div[@class = "info"]/div/a/@title')[0]                  #每个视频的标题
            region = item.xpath('div[@class = "info"]/div[1]/span[1]/text()')[0].strip('\n        ')          #每个视频的分类版块如动画
            view_num = item.xpath('div[@class = "info"]/div[3]/span[1]/text()')[0].strip('\n        ')         #每个视频的播放量
            danmu = item.xpath('div[@class = "info"]/div[3]/span[2]/text()')[0].strip('\n        ')         #弹幕
            upload_time  = item.xpath('div[@class = "info"]/div[3]/span[3]/text()')[0].strip('\n        ')  # 上传日期
            up_author = item.xpath('div[@class = "info"]/div[3]/span[4]/a/text()')[0].strip('\n        ')          #up主

            df = pd.DataFrame({'region': [region],'title': [title], 'view_num': [view_num], 'danmu': [danmu], 'upload_time': [upload_time], 'up_author': [up_author], 'video_url': [video_url]})
            result = pd.concat([result, df])

        time.sleep(random.random() + 1)
        print('已经完成b站第 {} 页爬取'.format(i))
    saveName = saveName + ".csv"
    result.to_csv(saveName, encoding='utf-8-sig',index=False)  # 保存为csv格式的文件
    return result

if __name__ == "__main__":
    keyword = input("请输入要搜索的关键词：")
    page = int(input("请输入要爬取的页数："))
    saveName = input("请输入要保存的文件名：")
    get_target(keyword, page,saveName)

#原文链接：https://blog.csdn.net/qq_44870829/article/details/111149808