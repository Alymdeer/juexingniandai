#!/usr/bin/env python
# coding: utf-8

# In[54]:


import requests
import pandas as pd
import datetime as dt
import numpy as np
import time
import sys


# In[55]:


#获取名单
infile=open("C:/Users/86181/Desktop/觉醒年代/觉醒年代及其主要人物表.txt",encoding='UTF-8')
namelist=infile.read().split('\n')[:-1]
infile.close()
namelist


# In[56]:


#https://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22%E8%A7%89%E9%86%92%E5%B9%B4%E4%BB%A3%22,%22wordType%22:1%7D]]&days=30


# In[57]:


headers={
    'Cookie':'BAIDUID=BDD927F62406E7B9C4F9ED067C7802F7:FG=1; PSTM=1597892836; BIDUPSID=D4CBA316EF73A2687242C3D94696A761; __yjs_duid=1_393c7a7d837bfcd50b61ad63cfeb20a61618366171168; BAIDUID_BFESS=BDD927F62406E7B9C4F9ED067C7802F7:FG=1; jsdk-uuid=8db18ada-d841-4a8c-bb8a-f32d973ae6be; BDUSS=TFVcFJ6dUlBZnhsLTF4Qjl6aU5PQy0yamU5cWRobndBb1Zna1pPZTNVNUt-UkZoRVFBQUFBJCQAAAAAAAAAAAEAAABtEjhfzaHw2NjoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEpw6mBKcOpgd; BDUSS_BFESS=TFVcFJ6dUlBZnhsLTF4Qjl6aU5PQy0yamU5cWRobndBb1Zna1pPZTNVNUt-UkZoRVFBQUFBJCQAAAAAAAAAAAEAAABtEjhfzaHw2NjoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEpw6mBKcOpgd; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; bdindexid=e10fb52e28lbgs1giqulvlsvb4; ai-studio-ticket=35F3A2E74CF94DBBB4F1B62D11F76AC0D67424D0A78F485C9332BB0C845431B9; BDRCVFR[k2U9xfnuVt6]=mk3SLVN4HKm; BDRCVFR[ueJalV_RTh0]=Sgq2UtKbV53nvGbpa4WUvY; H_PS_PSSID=; BDRCVFR[zmG01x_Fp5m]=dO4puMDy_impHNVmyb8mvqV; delPer=0; PSINO=1; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1626169542,1626238462; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1626169544,1626238467; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1626243137; RT="z=1&dm=baidu.com&si=0w55ywjp5dfb&ss=kr30e4xw&sl=z&tt=15k3&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1626244688; ab_sr=1.0.1_OTFiNzZjMWU3ZWZhYzkyMGRlZWQ0NWY0ZTQyNThhNzRjMDE4OWExOTI2ZmQ0YjYyOGQ3NTBlNGM1ZDE5NjJhNzMzNjExNTA2OGY2ZDI0NzJkYzgzNGVlN2MwYTE2YjMzZTQ0MGYwNzIyZDI0NzI4ZDM3Y2QzNWMyYjQ0YTIxNzYxYjRlOTU3OTcwNmFkMDZjZTNkM2E5YmEzZjI0NmE2Yg==; __yjs_st=2_MGU5OTY5NjdmNzU2YTAzNzk3MTVjNTIzYTljN2JiZTM4ODM3MWEyOTczMWE0ODE4ZDlkYjZiNzc0MWI1YmQ5NDU5NjdlYmVhZmEyZmNjMTk4MjIyNjRjMmFiMTU2Nzc0ZDA4NzU2OWUzNTk0NzlkZjFhOWI4NzEwODdhYTQ4N2YwYjFmNTUyOTYwNzdiMmU1Y2Q2ZDYwMzE4YzUxZDBlMGNhMmU1OGQ2NWExZGNmMWJiMzk1ZTEyNjljZTY3MDZhY2ExMjk3NWViZGRiZTBmZDIyYTM0ZTVmOTlmNmUwYjZkYzJhNjgwNjkzNTNmYjdkOWNiODA0ZjJmODZhZmZhNl83XzYzZDkxNzMx',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
}


# In[58]:


#爬取百度指数每日值
def decrypt(ptbk,data):
    d={}
    res=[]
    for i in range(len(ptbk)//2):
        d[ptbk[i]]=ptbk[len(ptbk)//2+i]
    for x in data:
        res.append(d[x])
    return "".join(res)

#第一种get_uniqid
#def get_ptbk(uniqid):
 #   url=f"https://index.baidu.com/Interface/ptbk?uniqid={uniqid}"
  #  response = requests.get(url,headers=headers)
   # return response.json().get('data')


#第二种方法get_uniqid
def get_ptbk(uniqid):
    url = 'https://index.baidu.com/Interface/ptbk?uniqid={}'
    resp = requests.get(url.format(uniqid), headers=headers)
    if resp.status_code != 200:
        print('获取uniqid失败')
        sys.exit(1)
    return resp.json().get('data')

def get_dailydata(keyword,start,end):
    url = f"https://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22{keyword}%22,%22wordType%22:1%7D]]&startDate={start}&endDate={end}"
    
    res=requests.get(url,headers=headers)
    j = res.json()
    
    uniqid = j.get('data').get('uniqid')
    ptbk = get_ptbk(uniqid)
    data = j.get('data').get('userIndexes')[0].get('all').get('data')
    res = decrypt(ptbk,data)
    return res


# In[59]:


#测试
#uniqid="efff99e79875ca1667c2c902307b91dd"
#data="Hw.cGcNHzcCMCNH1cCCGNHzMwMCNHwHcc7NH.zCCcNH1MwGcNHHG.MGNHHwc17NHHHwMwNH1.1.zNH.HCz.NHwC7GGNHzzCH1NHzM1H7NH.H71GN1Hz1w.N1HMcz1N1MwGwcNHGczHwNHCMG1.NH.77..NHw1wz1NH.z1w7NH.7CwwNHwH1C.NH.GczzNH1GcC1NH17CCHNH1H.wc"


# In[ ]:





# In[60]:


#测试
#ptbk=get_ptbk(uniqid)
#ptbk


# In[61]:


#测试
#decrypt(ptbk,data)


# In[62]:


#爬取多人的百度指数并制成字典
def make_dict(name_list,sy,sm,sd,ey,em,ed):
    start = str(dt.date(sy,sm,sd))
    end = str(dt.date(ey,em,ed))
    data_dict={}
    
    for name in name_list:
        print(name+'loading...')
        try:
            data_dict[name]=get_dailydata(name,start,end).split(',')
        except:
            break
        time.sleep(2)
    return data_dict


# In[68]:


data_d = make_dict(namelist,2021,6,14,2021,7,12)


# In[69]:


start=dt.date(2021,6,14)
end=dt.date(2021,7,13)
day_list=[]
for i in range(start.toordinal(),end.toordinal()):
    day_list.append(str(dt.date.fromordinal(i)))
day_list


# In[70]:


df=pd.DataFrame(data_d,index=day_list)
df


# In[75]:


#df[['曹汝霖']]


# In[76]:


df.replace('','0',inplace=True)


# In[77]:


df.transpose().to_excel("觉醒年代及其主要人物搜索指数.xls",encoding='UTF-8')


# In[ ]:




