#微博预登录;识别“展开全文”并爬取完整数据;翻页设置
#使用Selenium库，模拟真实用户对浏览器进行操作。

#导入selenium包
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

#打开页面
'''打开网址，预登陆'''
driver = webdriver.Edge()  #使用Edge浏览器
print('准备登陆Weibo.cn网站...')
# 发送请求
driver.get("https://login.sina.com.cn/signup/signin.php")
wait = WebDriverWait(driver, 5)
# 重要：暂停1分钟进行预登陆，此处填写账号密码及验证
time.sleep(60)

'''输入关键词到搜索框，完成搜索'''
# 使用selector去定位关键词搜索框
s_input = driver.find_element_by_css_selector('#search_input')
# 向搜索框中传入字段
s_input.send_keys("#觉醒年代#")
# 定位搜索键
confirm_btn = driver.find_element_by_css_selector('#search_submit')
# 点击
confirm_btn.click()

# 人为移动driver
driver.switch_to.window(driver.window_handles[1])

'''爬取第一页数据'''
comment = []
username = []

# 抓取节点：每个评论为一个节点（包括用户信息、评论、日期等信息），如果一页有20条评论，那么nodes的长度就为20
nodes = driver.find_elements_by_css_selector('div.card > div.card-feed > div.content')

# 对每个节点进行循环操作
for i in range(0, len(nodes), 1):
    # 判断每个节点是否有“展开全文”的链接
    flag = False
    try:
        nodes[i].find_element_by_css_selector("p>a[action-type='fl_unfold']").is_displayed()
        flag = True
    except:
        flag = False

    # 如果该节点具有“展开全文”的链接，且该链接中的文字是“展开全文c”，那么点击这个要素，并获取指定位置的文本；否则直接获取文本
    # （两个条件需要同时满足，因为该selector不仅标识了展开全文，还标识了其他元素，没有做到唯一定位）
    if (flag and nodes[i].find_element_by_css_selector("p>a[action-type='fl_unfold']").text.startswith('展开全文c')):
        nodes[i].find_element_by_css_selector("p>a[action-type='fl_unfold']").click()
        comment.append(nodes[i].find_element_by_css_selector('p[node-type="feed_list_content_full"]').text)
    else:
        comment.append(nodes[i].find_element_by_css_selector('p[node-type="feed_list_content"]').text)
    username.append(nodes[i].find_element_by_css_selector("div.info>div:nth-child(2)>a").text)

'''循环操作，获取剩余页数的数据，共爬取50页'''
for page in range(49):
    print(page)
    # 定位下一页按钮
    nextpage_button = driver.find_element_by_link_text('下一页')
    # 点击按键
    driver.execute_script("arguments[0].click();", nextpage_button)
    wait = WebDriverWait(driver, 5)
    # 与前面类似
    nodes1 = driver.find_elements_by_css_selector('div.card > div.card-feed > div.content')
    for i in range(0, len(nodes1), 1):
        flag = False
        try:
            nodes1[i].find_element_by_css_selector("p>a[action-type='fl_unfold']").is_displayed()
            flag = True

        except:
            flag = False
        if (flag and nodes1[i].find_element_by_css_selector("p>a[action-type='fl_unfold']").text.startswith('展开全文c')):
            nodes1[i].find_element_by_css_selector("p>a[action-type='fl_unfold']").click()
            comment.append(nodes1[i].find_element_by_css_selector('p[node-type="feed_list_content_full"]').text)
        else:
            comment.append(nodes1[i].find_element_by_css_selector('p[node-type="feed_list_content"]').text)
        username.append(nodes1[i].find_element_by_css_selector("div.info>div:nth-child(2)>a").text)

'''保存数据'''
data = pd.DataFrame({'username': username, 'comment': comment})
data.to_excel("#觉醒年代#.xlsx")