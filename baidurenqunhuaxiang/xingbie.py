import json
import pandas as pd
import requests
def baidu_gender_index(word, cookie):
    """
    百度指数 人群画像性别分布
    :param word: 关键词
    :param cookie:
    :return:
        desc    性别
        tgi     TGI指数
        word_rate   关键词分布比率
        all_rate    全网分布比率
        period      周期范围
    """
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Cookie": cookie,
            "DNT": "1",
            "Host": "zhishu.baidu.com",
            "Pragma": "no-cache",
            "Proxy-Connection": "keep-alive",
            "Referer": "zhishu.baidu.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        url = "http://index.baidu.com/api/SocialApi/baseAttributes?wordlist[]=%s" % word
        r = requests.get(url=url, headers=headers)
        data = json.loads(r.text)['data']
        period = "%s|%s" % (data['startDate'], data['endDate'])
        age_list = data['result'][0]['gender']
        age_df = pd.DataFrame(age_list)
        all_list = data['result'][1]['gender']
        all_df = pd.DataFrame(all_list)
        all_df.drop(["tgi", "typeId"], axis=1, inplace=True)
        res_df = pd.merge(age_df, all_df, on='desc')
        res_df['period'] = period
        res_df.drop(["typeId"], axis=1, inplace=True)
        res_df.rename(columns={'rate_x': 'word_rate', 'rate_y': 'all_rate'}, inplace=True)
        return res_df
    except:
        return None
if __name__ == "__main__":
    cookie = 'BIDUPSID=AA6ACB40BA91D8400799425B2165C78C; PSTM=1589373008; __yjs_duid=1_6f7a9a5697f1f46c538f72dd1522fbef1620059845652; BAIDUID=1421E8B162973B856BE738DAF923D17D:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=34099_33967_34004_34112_34072_34092_34111_26350_34244; bdindexid=huhasmgd91pd5jkatmj3169kr3; CHKFORREG=f7ff5de9ec28f179d65c4802ef0badef; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1626146255,1626265174,1626268167; BDUSS=hIcDkzOGdYNU4ySmFiRGlPbVBZUm9kQTltamVPSUNCNWdWbzVkZ2lLd29ieFpoRVFBQUFBJCQAAAAAAAAAAAEAAAAK~YCRtqu~qtDEufsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACji7mAo4u5gRl; BDUSS_BFESS=hIcDkzOGdYNU4ySmFiRGlPbVBZUm9kQTltamVPSUNCNWdWbzVkZ2lLd29ieFpoRVFBQUFBJCQAAAAAAAAAAAEAAAAK~YCRtqu~qtDEufsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACji7mAo4u5gRl; delPer=0; PSINO=2; BAIDUID_BFESS=1421E8B162973B856BE738DAF923D17D:FG=1; BDRCVFR[8gzLr2xelNt]=mk3SLVN4HKm; BA_HECTOR=ahag818g008g2021hj1geu1sc0r; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1626278983; ab_sr=1.0.1_NzhjNGFmN2I0MTkyYTI1NWZjYWFkOTIwNDc5NzU5OTc5Nzc2MTlkNDU0ZTU2MDlmNGVkZjhkNjJlNjFjZWNmYzNkMmQ2ZWM0MDY0YWE5NzYyMDBjYTA0ZjM1YzQxZWVlY2JkOGI2YjE2YTRjZmFkNGY2NTE4Zjk1YTE4M2RiMmRlMWIwZTM1YTA3YTRhNWM5YzZlYmE4YWYwODg5ZmQxMg==; __yjs_st=2_ZmFiNTY2ZWIwOWNlYTczYjliM2M4YjQ5OTNhMzM3YzgzNzY3NzdlNTVhODgwZWUyMGNkNzA4MDAzZDRjYjgwMGYxZjc5Zjc0NTk2NTljOGM2OWM1ZmFjZjRlN2M4NzIwYmNlYjMzZjQ4YmE4MWE3MDUwZGFkY2Y1ODY2MTZlNTY5Yjc1NTI2MjVkNjRiYjVkYjA1MzhlODc5ZjhjNjFkNWJjYjc3MGI1YzI1NGRmNGE2ZmNhMjY0ZTJlMDlmNGNlYTUzMThlOWY3ZjFjMDBjMmI2NTcyZWE3ODFhOTQxNmJjNjhmN2U5MTRmZDdkNTVlYzUxYzdjYzVlNTY0OGI3OF83X2Y1NzQ3OTI1; RT="z=1&dm=baidu.com&si=n9o75azchwt&ss=kr3oilqt&sl=2&tt=18u&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=97q'
    data = baidu_gender_index( "觉醒年代", cookie )
    fileName = 'gender.csv'
    with open( fileName, 'w', encoding='utf-8' ) as f:
        f.write(str(data))
