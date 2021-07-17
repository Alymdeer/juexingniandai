import json
import pandas as pd
import requests
def decrypt(t: str, e: str) -> str:
    """
    解密函数
    :param t:
    :type t:
    :param e:
    :type e:
    :return:
    :rtype:
    """
    n, i, a, result = list(t), list(e), {}, []
    ln = int(len(n) / 2)
    start, end = n[ln:], n[:ln]
    a = dict(zip(end, start))
    return "".join([a[j] for j in e])
def baidu_areas_index(word, cookie):
    """
    百度指数 人群画像地域分布
    :param word: 关键词
    :param cookie:
    :return:
        prov    省份
        city    城市
        period    周期范围
        prov_number   省份数据
        city_number   城市数据
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
        url = "https://index.baidu.com/api/SocialApi/region?region=0&word=%s&startDate=2021-02-01&endDate=2021-07-14&days=" % word
        r = requests.get(url=url, headers=headers)
        data = json.loads(r.text)['data']
        print(data)
        period = data['region']['period']
        prov_dict=json.loads(data['region']['prov'])
        prov_keys=prov_dict.keys()
        prov= pd.DataFrame(prov_keys)
        prov_list=prov_dict.values()
        prov_df = pd.DataFrame(prov_list)
        city_dict = json.loads(data['region']['city'])
        city_keys=city_dict.keys()
        city= pd.DataFrame(city_keys)
        city_list=city_dict.values()
        city_df = pd.DataFrame(city_list)
        res_df=pd.merge(prov_df,city_df,left_on='prov',right_on='city')
        res_df['period'] = period
        res_df['prov'] = prov
        res_df['city'] = city
        res_df.rename(columns={'number_x': 'prov_number','number_y': 'city_number'},inplace=True)
        return res_df
    except:
        return None
#if __name__ == "__main__":
  #  cookie ='BIDUPSID=AA6ACB40BA91D8400799425B2165C78C; PSTM=1589373008; HOSUPPORT=1; HOSUPPORT_BFESS=1; ' \
   #         '__yjs_duid=1_6f7a9a5697f1f46c538f72dd1522fbef1620059845652; BAIDUID=1421E8B162973B856BE738DA' \
    #        'F923D17D:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=34099_33967_34004_34112_340' \
     #       '72_34092_34111_26350_34244; bdindexid=huhasmgd91pd5jkatmj3169kr3; BAIDUID_BFESS=1421E8B162973' \
      #      'B856BE738DAF923D17D:FG=1; delPer=0; PSINO=2; BA_HECTOR=8h050gagaha4258k9s1getnuj0q; USERNAMET' \
       #     'YPE=3; USERNAMETYPE_BFESS=3; Hm_lvt_90056b3f84f90da57dc0f40150f005d5=1626268095; Hm_lpvt_9005' \
       #     '6b3f84f90da57dc0f40150f005d5=1626268095; logTraceID=ad7e4ad46767811395082aaa0dd9e122d98adc0d3' \
        #    '0f271a5e7; UBI=fi_PncwhpxZ%7ETaL93nw07FCQCUI1djMQUOak3w3QTo0Xiq1el75OoSeSnXfmdjiG%7EydVoN1IKkG' \
        #    'Z4SJ5Xf7XdMVNtT%7EdzopDX-Tw08p8EAyf6jtmEcZLRWvzNYxY95PWz%7EfLl9gS1E1PKXWJp1YH1WKljDYaOaaDdjQfo' \
         #   'adD5CDQB-RfzfWwfSTKCUrLgFO%7EYJ%7EIX%7EiyBtjP5TzUKA8d0e04hzKIQ4I0tTmRCGj; UBI_BFESS=fi_Pncwhpx' \
         #   'Z%7ETaL93nw07FCQCUI1djMQUOak3w3QTo0Xiq1el75OoSeSnXfmdjiG%7EydVoN1IKkGZ4SJ5Xf7XdMVNtT%7EdzopDX-' \
         #   'Tw08p8EAyf6jtmEcZLRWvzNYxY95PWz%7EfLl9gS1E1PKXWJp1YH1WKljDYaOaaDdjQfoadD5CDQB-RfzfWwfSTKCUrLg' \
         #   'FO%7EYJ%7EIX%7EiyBtjP5TzUKA8d0e04hzKIQ4I0tTmRCGj; SAVEUSERID=8a330160a4b6c2d167db84d03dde5d;' \
          #  ' HISTORY=963db9c3a048223535ccca537567dd954c0d1426e4dc71c6b128d37f9ffff73d70; SAVEUSERID_BFESS' \
           # '=8a330160a4b6c2d167db84d03dde5d; HISTORY_BFESS=963db9c3a048223535ccca537567dd954c0d1426e4dc71c' \
          #  '6b128d37f9ffff73d70; BDUSS=6ite3u7a66n3f5ome0hfvbm9e0; BDUSS_BFESS=6ite3u7a66n3f5ome0hfvbm9e0;' \
        #    ' ab_sr=1.0.1_MTQ4OGVlYTBjNDI1Mzc5ZGExMDgwNmFmNTBmNGFmM2UxODJjZWE1YWJhOTgwMjk3ZTUyMmY1MWU4MDkyN' \
        #    'DM4OTJjOWY2YWVkYWU5OGM3OWYxMDQ1MzYzYWI1ODlmY2YxOTUwNWI4NTNiYmQ1MTAyNzNlMzQ4N2NjMjAzMGM4N2NjOGI' \
        #   '0MWM1ZGEzNzNlYmQwM2Y0MzcxYWE0YzZmMjQ3OQ==; __yjs_st=2_ZmFiNTY2ZWIwOWNlYTczYjliM2M4YjQ5OTNhMzM3' \
        #    'YzgzNzY3NzdlNTVhODgwZWUyMGNkNzA4MDAzZDRjYjgwMGYxZjc5Zjc0NTk2NTljOGM2OWM1ZmFjZjRlN2M4NzIwYmNlYj' \
         #   'MzZjQ4YmE4MWE3MDUwZGFkY2Y1ODY2MTZlNTY5Yjc1NTI2MjVkNjRiYjVkYjA1MzhlODc5ZjhjNjFkNWJjYjc3MGI1YzI1' \
         #   'NGRmNGE2ZmNhMjY0ZTJlMDlmNGNlOWJkODVkNDRjYTFhZGI4OGE2NDdjNWQ0ZWJiMGFmNzUzNGQ4ODAzYjhlMGRiZmVhYW' \
          #  'EwNzRkN2M0ZTVmMWFjYl83X2YyMGQwMzI4; RT="sl=g&ss=kr3htr7f&tt=5ei&bcn=https%3A%2F%2Ffclog.baidu.' \
           # 'com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=onypyhhjqbg&ld=9f43"; pplogid=8790LZhD6' \
          #  '6HJoko2BeMKLZs5F9DCKkqVdhY0%2FzmBximOeojsTZ1kUfYB8bYXv8qeY29VbXbQijuTHsDwDCZatLE70%2FmBRxiCC2R' \
           # 'NIAJ8RP0F0%2Fk%3D; pplogid_BFESS=8790LZhD66HJoko2BeMKLZs5F9DCKkqVdhY0%2FzmBximOeojsTZ1kUfYB8b' \
            #'YXv8qeY29VbXbQijuTHsDwDCZatLE70%2FmBRxiCC2RNIAJ8RP0F0%2Fk%3D'
 #   data4=baidu_areas_index(word="觉醒年代",cookie=cookie)
 #   print(data4)