import requests
from baidu_id import province, city
def cityzh(place):
    global area
    if place == '安徽':
        area = 928
    if place == '澳门':
        area = 934
    if place == '北京':
        area = 911
    if place == '重庆':
        area = 904
    if place == '福建':
        area = 909
    if place == '广东':
        area = 913
    if place == '广西':
        area = 912
    if place == '甘肃':
        area = 925
    if place == '贵州':
        area = 902
    if place == '河北':
        area = 920
    if place == '黑龙江':
        area = 921
    if place == '河南':
        area = 927
    if place == '湖南':
        area = 908
    if place == '湖北':
        area = 906
    if place == '海南':
        area = 930
    if place == '吉林':
        area = 922
    if place == '江苏':
        area = 916
    if place == '江西':
        area = 903
    if place == '辽宁':
        area = 907
    if place == '内蒙古':
        area = 905
    if place == '宁夏':
        area = 919
    if place == '青海':
        area = 918
    if place == '上海':
        area = 910
    if place == '四川':
        area = 914
    if place == '山东':
        area = 901
    if place == '山西':
        area = 929
    if place == '陕西':
        area = 924
    if place == '天津':
        area = 923
    if place == '台湾':
        area = 931
    if place == '西藏':
        area = 932
    if place == '香港':
        area = 933
    if place == '新疆':
        area = 926
    if place == '云南':
        area = 915
    if place == '浙江':
        area = 917
    return area
def get_rep_json(url):
    """
    获取json
    :param url: 请求接口
    :return:
    """
    hearder = {
        "Cookie":'BIDUPSID=AA6ACB40BA91D8400799425B2165C78C; PSTM=1589373008; __yjs_duid=1_6f7a9a5697f1f46c538f72dd1522fbef1620059845652; BAIDUID=1421E8B162973B856BE738DAF923D17D:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ai-studio-ticket=6B753BD18F854EDD8776310B1518A8B7C7921533AAAE433B94A5A713F35F5101; BAIDUID_BFESS=1421E8B162973B856BE738DAF923D17D:FG=1; BDRCVFR[8gzLr2xelNt]=mk3SLVN4HKm; delPer=0; PSINO=2; H_PS_PSSID=34099_33967_34004_34072_34092_34111_26350_34244; BA_HECTOR=a48ka40g8h258g85e11gf4t2j0r; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1626419421,1626448054,1626502229,1626502433; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1626502447; BDUSS=nhhSTFUUG9IclphYX5sYjdpdm1qUThtQThYZDhyTm44U3RteUlhOURmWUhBeHBoRUFBQUFBJCQAAAAAAQAAAAEAAAD0TnIA8LDO9eihAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd28mAHdvJgY; BDUSS_BFESS=nhhSTFUUG9IclphYX5sYjdpdm1qUThtQThYZDhyTm44U3RteUlhOURmWUhBeHBoRUFBQUFBJCQAAAAAAQAAAAEAAAD0TnIA8LDO9eihAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd28mAHdvJgY; ab_sr=1.0.1_MDAxYjM5MTU2OGMxNTIzNmJlNDc1NWJkOTFmZDkxM2U4NjM4YmRhMzQzN2JmZDA3YzdjODE5N2I0ZDgwMDY0ZmFmZDFiM2ZhNTJjMDU0N2RkYzg5OTRjNjc5NjM0MzExNGUxNjU4YmQ5MTQ4NjQyNGI1YzRlYTc2YWRlMzM1OTY3ZmY3ZTE0NDA4M2E3ZGEyNzYzMTYzOGQ2Yjk2ZGEzYg==; __yjs_st=2_ZmFiNTY2ZWIwOWNlYTczYjliM2M4YjQ5OTNhMzM3YzgzNzY3NzdlNTVhODgwZWUyMGNkNzA4MDAzZDRjYjgwMGYxZjc5Zjc0NTk2NTljOGM2OWM1ZmFjZjRlN2M4NzIwYmNlYjMzZjQ4YmE4MWE3MDUwZGFkY2Y1ODY2MTZlNTY5Yjc1NTI2MjVkNjRiYjVkYjA1MzhlODc5ZjhjNjFkNWJjYjc3MGI1YzI1NGRmNGE2ZmNhMjY0ZTJlMDlmNGNlOTlkZTA4MzZmZTliYzIwYjFlOWI1Nzk1ZTVmZDFhYjAwOWFjZWUxODM1YTM3NDU2ZmJhOWEzZDk1ZWRlM2RiNF83Xzc4Yzg0YmQw; RT="z=1&dm=baidu.com&si=qjvtrzlnmeo&ss=kr7dfjty&sl=j&tt=b8d&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4por&ul=9dwv',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    response = requests.get(url, headers=hearder)
    response_data = response.json()
    return response_data
def baidu_province_index(word,startDate,endDate):
    """
    百度指数 人群画像地域全国分布
    """
    url = f"http://index.baidu.com/api/SearchApi/region?region=0&word={word}&startDate={startDate}&endDate={endDate}"
    region = get_rep_json(url)['data']['region'][0]
    region_city = [{'city': city[int( city_n )], 'number': region['city'][city_n]} for city_n in region['city']]
    region_prov = [{'prov': province[int( prov_n )], 'number': region['prov'][prov_n]} for prov_n in region['prov']]
    return region_city, region_prov
def baidu_city_index(word,place,startDate,endDate):
    """
    百度指数 人群画像地域城市分布
    """
    global area
    area = cityzh( place )
    url = f"http://index.baidu.com/api/SearchApi/region?region={area}&word={word}&startDate={startDate}&endDate={endDate}"
    region = get_rep_json(url)['data']['region'][0]
    region_city = [{'city': city[int( city_n )], 'number': region['city'][city_n]} for city_n in region['city']]
    return region_city
if __name__ == "__main__":
    data=baidu_province_index('觉醒年代','2021-02-01','2021-07-16')
    fileName = 'areas.csv'
    with open( fileName, 'w', encoding='utf-8' ) as f:
        f.write( str(data))
    print('保存了全国的csv文件')
    shuju = {}
    place_list = {'安徽', '澳门', '北京', '重庆', '福建', '广东', '广西', '甘肃', '贵州', '河北', '黑龙江', '河南', '湖南', '湖北', '海南', '吉林',
                  '江苏', '江西', '辽宁', '内蒙古', '宁夏', '青海', '上海', '四川', '山东', '山西', '陕西', '天津', '台湾', '西藏', '香港', '新疆', '云南',
                  '浙江'}
    for p in place_list:
        shuju[p]=baidu_city_index( "觉醒年代",p,'2021-02-01', '2021-07-16')
        fileName2= 'prov'+p+'.csv'
        with open( fileName2, 'w', encoding='utf-8' ) as f:
            f.write( str( shuju[p] ) )
            print( "保存了%s的csv文件" %p)
    print("保存完毕")

