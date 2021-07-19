import requests
import random
from bs4 import BeautifulSoup
def getComments(id,pageNum):
    movieComments = ""
    for i in range(pageNum):
        start = i*20
        url = "https://movie.douban.com/subject/"+str(id)+"/comments?start="+str(start)+"&limit=20&sort=new_score&status=P"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
        }
        print("正在爬取第%s页评论" % (i+1))
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text,'lxml')
        commentsList = soup.find_all('span',class_ ='short')
        for comments in commentsList:
            movieComments += comments.text
            movieComments += '\n'
    return movieComments

def saveComments(Comments):
    try:
        fileName = 'movieComments.txt'
        with open(fileName,'w',encoding='utf-8') as f:
            f.write(str(Comments))
        print('保存成功！')
    except:
        print('保存失败！')

if __name__ == '__main__':
    id = '30228394'
    pageNum=random.randint(10,50)
    Comments = getComments(id,pageNum)
    saveComments(Comments)
from jieba.analyse import *

keyWord = []
def getData():
    with open('movieComments.txt',encoding = 'utf-8') as f:
        data = f.read()
    for keyword in extract_tags(data, topK=100):
        keyWord.append(keyword)
def saveData(keyWord):
   with open('TF-IDFanalyse.txt','w') as f:
        for i in range(len(keyWord)):
            f.write(str(i+1)+'.'+str(keyWord[i]))
            f.write('\n')
if __name__ == '__main__':
    getData()
    saveData(keyWord)
    print('保存成功！')
