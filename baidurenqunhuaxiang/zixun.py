import pandas as pd
import requests


def cityzh(place):
    global area
    if place == '全国':
        area = 0
    if place == '安徽':
        area = 928
    if place == '安徽-合肥':
        area = 189
    if place == '安徽-铜陵':
        area = 173
    if place == '安徽-黄山':
        area = 174
    if place == '安徽-池州':
        area = 175
    if place == '安徽-宣城':
        area = 176
    if place == '安徽-巢湖':
        area = 177
    if place == '安徽-淮南':
        area = 178
    if place == '安徽-宿州':
        area = 179
    if place == '安徽-六安':
        area = 181
    if place == '安徽-滁州':
        area = 182
    if place == '安徽-淮北':
        area = 183
    if place == '安徽-阜阳':
        area = 184
    if place == '安徽-马鞍山':
        area = 185
    if place == '安徽-安庆':
        area = 186
    if place == '安徽-蚌埠':
        area = 187
    if place == '安徽-芜湖':
        area = 188
    if place == '安徽-亳州':
        area = 391
    if place == '澳门':
        area = 934
    if place == '北京':
        area = 911
    if place == '重庆':
        area = 904
    if place == '福建':
        area = 909
    if place == '福建-福州':
        area = 50
    if place == '福建-莆田':
        area = 51
    if place == '福建-三明':
        area = 52
    if place == '福建-龙岩':
        area = 53
    if place == '福建-厦门':
        area = 54
    if place == '福建-泉州':
        area = 55
    if place == '福建-漳州':
        area = 56
    if place == '福建-宁德':
        area = 87
    if place == '福建-南平':
        area = 253
    if place == '广东':
        area = 913
    if place == '广东-广州':
        area = 95
    if place == '广东-深圳':
        area = 94
    if place == '广东-东莞':
        area = 133
    if place == '广东-云浮':
        area = 195
    if place == '广东-佛山':
        area = 196
    if place == '广东-湛江':
        area = 197
    if place == '广东-江门':
        area = 198
    if place == '广东-惠州':
        area = 199
    if place == '广东-珠海':
        area = 200
    if place == '广东-韶关':
        area = 201
    if place == '广东-阳江':
        area = 202
    if place == '广东-茂名':
        area = 203
    if place == '广东-潮州':
        area = 204
    if place == '广东-揭阳':
        area = 205
    if place == '广东-中山':
        area = 207
    if place == '广东-清远':
        area = 208
    if place == '广东-肇庆':
        area = 209
    if place == '广东-河源':
        area = 210
    if place == '广东-梅州':
        area = 211
    if place == '广东-汕头':
        area = 212
    if place == '广东-汕尾':
        area = 213
    if place == '广西':
        area = 912
    if place == '广西-南宁':
        area = 90
    if place == '广西-柳州':
        area = 89
    if place == '广西-桂林':
        area = 91
    if place == '广西-贺州':
        area = 92
    if place == '广西-贵港':
        area = 93
    if place == '广西-玉林':
        area = 118
    if place == '广西-河池':
        area = 119
    if place == '广西-北海':
        area = 128
    if place == '广西-钦州':
        area = 129
    if place == '广西-防城港':
        area = 130
    if place == '广西-百色':
        area = 131
    if place == '广西-梧州':
        area = 132
    if place == '广西-来宾':
        area = 506
    if place == '广西-崇左':
        area = 665
    if place == '甘肃':
        area = 925
    if place == '甘肃-兰州':
        area = 166
    if place == '甘肃-庆阳':
        area = 281
    if place == '甘肃-定西':
        area = 282
    if place == '甘肃-武威':
        area = 283
    if place == '甘肃-酒泉':
        area = 284
    if place == '甘肃-张掖':
        area = 285
    if place == '甘肃-嘉峪关':
        area = 286
    if place == '甘肃-平凉':
        area = 307
    if place == '甘肃-天水':
        area = 308
    if place == '甘肃-白银':
        area = 309
    if place == '甘肃-金昌':
        area = 343
    if place == '甘肃-陇南':
        area = 344
    if place == '甘肃-临夏':
        area = 346
    if place == '甘肃-甘南':
        area = 673
    if place == '贵州':
        area = 902
    if place == '贵州-贵阳':
        area = 2
    if place == '贵州-黔南':
        area = 3
    if place == '贵州-六盘水':
        area = 4
    if place == '贵州-遵义':
        area = 59
    if place == '贵州-黔东南':
        area = 61
    if place == '贵州-铜仁':
        area = 422
    if place == '贵州-安顺':
        area = 424
    if place == '贵州-毕节':
        area = 426
    if place == '贵州-黔西南':
        area = 588
    if place == '河北':
        area = 920
    if place == '河北-石家庄':
        area = 141
    if place == '河北-衡水':
        area = 143
    if place == '河北-张家口':
        area = 144
    if place == '河北-承德':
        area = 145
    if place == '河北-秦皇岛':
        area = 146
    if place == '河北-廊坊':
        area = 147
    if place == '河北-沧州':
        area = 148
    if place == '河北-保定':
        area = 259
    if place == '河北-唐山':
        area = 261
    if place == '河北-邯郸':
        area = 292
    if place == '河北-邢台':
        area = 293
    if place == '黑龙江':
        area = 921
    if place == '黑龙江-哈尔滨':
        area = 152
    if place == '黑龙江-大庆':
        area = 153
    if place == '黑龙江-伊春':
        area = 295
    if place == '黑龙江-大兴安岭':
        area = 297
    if place == '黑龙江-黑河':
        area = 300
    if place == '黑龙江-鹤岗':
        area = 301
    if place == '黑龙江-七台河':
        area = 302
    if place == '黑龙江-齐齐哈尔':
        area = 319
    if place == '黑龙江-佳木斯':
        area = 320
    if place == '黑龙江-牡丹江':
        area = 322
    if place == '黑龙江-鸡西':
        area = 323
    if place == '黑龙江-绥化':
        area = 324
    if place == '黑龙江-双鸭山':
        area = 359
    if place == '河南':
        area = 927
    if place == '河南-郑州':
        area = 168
    if place == '河南-南阳':
        area = 262
    if place == '河南-新乡':
        area = 263
    if place == '河南-开封':
        area = 264
    if place == '河南-焦作':
        area = 265
    if place == '河南-平顶山':
        area = 266
    if place == '河南-许昌':
        area = 268
    if place == '河南-安阳':
        area = 370
    if place == '河南-驻马店':
        area = 371
    if place == '河南-信阳':
        area = 373
    if place == '河南-鹤壁':
        area = 374
    if place == '河南-周口':
        area = 375
    if place == '河南-商丘':
        area = 376
    if place == '河南-洛阳':
        area = 378
    if place == '河南-漯河':
        area = 379
    if place == '河南-濮阳':
        area = 380
    if place == '河南-三门峡':
        area = 381
    if place == '河南-济源':
        area = 667
    if place == '湖南':
        area = 908
    if place == '湖南-长沙':
        area = 43
    if place == '湖南-岳阳':
        area = 44
    if place == '湖南-衡阳':
        area = 45
    if place == '湖南-株洲':
        area = 46
    if place == '湖南-湘潭':
        area = 47
    if place == '湖南-益阳':
        area = 48
    if place == '湖南-郴州':
        area = 49
    if place == '湖南-湘西':
        area = 65
    if place == '湖南-娄底':
        area = 66
    if place == '湖南-怀化':
        area = 67
    if place == '湖南-常德':
        area = 68
    if place == '湖南-张家界':
        area = 226
    if place == '湖南-永州':
        area = 269
    if place == '湖南-邵阳':
        area = 405
    if place == '湖北':
        area = 906
    if place == '湖北-武汉':
        area = 28
    if place == '湖北-黄石':
        area = 30
    if place == '湖北-荆州':
        area = 31
    if place == '湖北-襄阳':
        area = 32
    if place == '湖北-黄冈':
        area = 33
    if place == '湖北-荆门':
        area = 34
    if place == '湖北-宜昌':
        area = 35
    if place == '湖北-十堰':
        area = 36
    if place == '湖北-随州':
        area = 37
    if place == '湖北-恩施':
        area = 38
    if place == '湖北-鄂州':
        area = 39
    if place == '湖北-咸宁':
        area = 40
    if place == '湖北-孝感':
        area = 41
    if place == '湖北-仙桃':
        area = 42
    if place == '湖北-天门':
        area = 73
    if place == '湖北-潜江':
        area = 74
    if place == '湖北-神农架':
        area = 687
    if place == '海南':
        area = 930
    if place == '海南-海口':
        area = 239
    if place == '海南-万宁':
        area = 241
    if place == '海南-琼海':
        area = 242
    if place == '海南-三亚':
        area = 243
    if place == '海南-儋州':
        area = 244
    if place == '海南-东方':
        area = 456
    if place == '海南-五指山':
        area = 582
    if place == '海南-文昌':
        area = 670
    if place == '海南-陵水':
        area = 674
    if place == '海南-澄迈':
        area = 675
    if place == '海南-乐东':
        area = 679
    if place == '海南-临高':
        area = 680
    if place == '海南-定安':
        area = 681
    if place == '海南-昌江':
        area = 683
    if place == '海南-屯昌':
        area = 684
    if place == '海南-保亭':
        area = 686
    if place == '海南-白沙':
        area = 689
    if place == '海南-琼中':
        area = 690
    if place == '吉林':
        area = 922
    if place == '吉林-长春':
        area = 154
    if place == '吉林-四平':
        area = 155
    if place == '吉林-辽源':
        area = 191
    if place == '吉林-松原':
        area = 194
    if place == '吉林-吉林':
        area = 270
    if place == '吉林-通化':
        area = 407
    if place == '吉林-白山':
        area = 408
    if place == '吉林-白城':
        area = 410
    if place == '吉林-延边':
        area = 525
    if place == '江苏':
        area = 916
    if place == '江苏-南京':
        area = 125
    if place == '江苏-苏州':
        area = 126
    if place == '江苏-无锡':
        area = 127
    if place == '江苏-连云港':
        area = 156
    if place == '江苏-淮安':
        area = 157
    if place == '江苏-扬州':
        area = 158
    if place == '江苏-泰州':
        area = 159
    if place == '江苏-盐城':
        area = 160
    if place == '江苏-徐州':
        area = 161
    if place == '江苏-常州':
        area = 162
    if place == '江苏-南通':
        area = 163
    if place == '江苏-镇江':
        area = 169
    if place == '江苏-宿迁':
        area = 172
    if place == '江西':
        area = 903
    if place == '江西-南昌':
        area = 5
    if place == '江西-九江':
        area = 6
    if place == '江西-鹰潭':
        area = 7
    if place == '江西-抚州':
        area = 8
    if place == '江西-上饶':
        area = 9
    if place == '江西-赣州':
        area = 10
    if place == '江西-吉安':
        area = 115
    if place == '江西-萍乡':
        area = 136
    if place == '江西-景德镇':
        area = 137
    if place == '江西-新余':
        area = 246
    if place == '江西-宜春':
        area = 256
    if place == '辽宁':
        area = 907
    if place == '辽宁-沈阳':
        area = 150
    if place == '辽宁-大连':
        area = 29
    if place == '辽宁-盘锦':
        area = 151
    if place == '辽宁-鞍山':
        area = 215
    if place == '辽宁-朝阳':
        area = 216
    if place == '辽宁-锦州':
        area = 217
    if place == '辽宁-铁岭':
        area = 218
    if place == '辽宁-丹东':
        area = 219
    if place == '辽宁-本溪':
        area = 220
    if place == '辽宁-营口':
        area = 221
    if place == '辽宁-抚顺':
        area = 222
    if place == '辽宁-阜新':
        area = 223
    if place == '辽宁-辽阳':
        area = 224
    if place == '辽宁-葫芦岛':
        area = 225
    if place == '内蒙古':
        area = 905
    if place == '内蒙古-呼和浩特':
        area = 20
    if place == '内蒙古-包头':
        area = 13
    if place == '内蒙古-鄂尔多斯':
        area = 14
    if place == '内蒙古-巴彦淖尔':
        area = 15
    if place == '内蒙古-乌海':
        area = 16
    if place == '内蒙古-阿拉善盟':
        area = 17
    if place == '内蒙古-锡林郭勒盟':
        area = 19
    if place == '内蒙古-赤峰':
        area = 21
    if place == '内蒙古-通辽':
        area = 22
    if place == '内蒙古-呼伦贝尔':
        area = 25
    if place == '内蒙古-乌兰察布':
        area = 331
    if place == '内蒙古-兴安盟':
        area = 333
    if place == '宁夏':
        area = 919
    if place == '宁夏-银川':
        area = 140
    if place == '宁夏-吴忠':
        area = 395
    if place == '宁夏-固原':
        area = 396
    if place == '宁夏-石嘴山':
        area = 472
    if place == '宁夏-中卫':
        area = 480
    if place == '青海':
        area = 918
    if place == '青海-西宁':
        area = 139
    if place == '青海-海西':
        area = 608
    if place == '青海-海东':
        area = 652
    if place == '青海-玉树':
        area = 659
    if place == '青海-海南':
        area = 676
    if place == '青海-海北':
        area = 682
    if place == '青海-黄南':
        area = 685
    if place == '青海-果洛':
        area = 688
    if place == '上海':
        area = 910
    if place == '四川':
        area = 914
    if place == '四川-成都':
        area = 97
    if place == '四川-宜宾':
        area = 96
    if place == '四川-绵阳':
        area = 98
    if place == '四川-广元':
        area = 99
    if place == '四川-遂宁':
        area = 100
    if place == '四川-巴中':
        area = 101
    if place == '四川-内江':
        area = 102
    if place == '四川-泸州':
        area = 103
    if place == '四川-南充':
        area = 104
    if place == '四川-德阳':
        area = 106
    if place == '四川-乐山':
        area = 107
    if place == '四川-广安':
        area = 108
    if place == '四川-资阳':
        area = 109
    if place == '四川-自贡':
        area = 111
    if place == '四川-攀枝花':
        area = 112
    if place == '四川-达州':
        area = 113
    if place == '四川-雅安':
        area = 114
    if place == '四川-眉山':
        area = 291
    if place == '四川-甘孜':
        area = 417
    if place == '四川-阿坝':
        area = 457
    if place == '四川-凉山':
        area = 479
    if place == '山东':
        area = 901
    if place == '山东-济南':
        area = 1
    if place == '山东-滨州':
        area = 76
    if place == '山东-青岛':
        area = 77
    if place == '山东-烟台':
        area = 78
    if place == '山东-临沂':
        area = 79
    if place == '山东-潍坊':
        area = 80
    if place == '山东-淄博':
        area = 81
    if place == '山东-东营':
        area = 82
    if place == '山东-聊城':
        area = 83
    if place == '山东-菏泽':
        area = 84
    if place == '山东-枣庄':
        area = 85
    if place == '山东-德州':
        area = 86
    if place == '山东-威海':
        area = 88
    if place == '山东-济宁':
        area = 352
    if place == '山东-泰安':
        area = 353
    if place == '山东-莱芜':
        area = 356
    if place == '山东-日照':
        area = 366
    if place == '山西':
        area = 929
    if place == '山西-太原':
        area = 231
    if place == '山西-大同':
        area = 227
    if place == '山西-长治':
        area = 228
    if place == '山西-忻州':
        area = 229
    if place == '山西-晋中':
        area = 230
    if place == '山西-临汾':
        area = 232
    if place == '山西-运城':
        area = 233
    if place == '山西-晋城':
        area = 234
    if place == '山西-朔州':
        area = 235
    if place == '山西-阳泉':
        area = 236
    if place == '山西-吕梁':
        area = 237
    if place == '陕西':
        area = 924
    if place == '陕西-西安':
        area = 165
    if place == '陕西-铜川':
        area = 271
    if place == '陕西-安康':
        area = 272
    if place == '陕西-宝鸡':
        area = 273
    if place == '陕西-商洛':
        area = 274
    if place == '陕西-渭南':
        area = 275
    if place == '陕西-汉中':
        area = 276
    if place == '陕西-咸阳':
        area = 277
    if place == '陕西-榆林':
        area = 278
    if place == '陕西-延安':
        area = 401
    if place == '天津':
        area = 923
    if place == '台湾':
        area = 931
    if place == '西藏':
        area = 932
    if place == '西藏-拉萨':
        area = 466
    if place == '西藏-日喀则':
        area = 516
    if place == '西藏-那曲':
        area = 655
    if place == '西藏-林芝':
        area = 656
    if place == '西藏-山南':
        area = 677
    if place == '西藏-昌都':
        area = 678
    if place == '西藏-阿里':
        area = 691
    if place == '香港':
        area = 933
    if place == '新疆':
        area = 926
    if place == '新疆-乌鲁木齐':
        area = 467
    if place == '新疆-石河子':
        area = 280
    if place == '新疆-吐鲁番':
        area = 310
    if place == '新疆-昌吉':
        area = 311
    if place == '新疆-哈密':
        area = 312
    if place == '新疆-阿克苏':
        area = 315
    if place == '新疆-克拉玛依':
        area = 317
    if place == '新疆-博尔塔拉':
        area = 318
    if place == '新疆-阿勒泰':
        area = 383
    if place == '新疆-喀什':
        area = 384
    if place == '新疆-和田':
        area = 386
    if place == '新疆-巴音郭楞':
        area = 499
    if place == '新疆-伊犁':
        area = 520
    if place == '新疆-塔城':
        area = 563
    if place == '新疆-克孜勒苏柯尔克孜':
        area = 653
    if place == '新疆-五家渠':
        area = 661
    if place == '新疆-阿拉尔':
        area = 692
    if place == '新疆-图木舒克':
        area = 693
    if place == '云南':
        area = 915
    if place == '云南-昆明':
        area = 117
    if place == '云南-玉溪':
        area = 123
    if place == '云南-楚雄':
        area = 124
    if place == '云南-大理':
        area = 334
    if place == '云南-昭通':
        area = 335
    if place == '云南-红河':
        area = 337
    if place == '云南-曲靖':
        area = 339
    if place == '云南-丽江':
        area = 342
    if place == '云南-临沧':
        area = 350
    if place == '云南-文山':
        area = 437
    if place == '云南-保山':
        area = 438
    if place == '云南-普洱':
        area = 666
    if place == '云南-西双版纳':
        area = 668
    if place == '云南-德宏':
        area = 669
    if place == '云南-怒江':
        area = 671
    if place == '云南-迪庆':
        area = 672
    if place == '浙江':
        area = 917
    if place == '浙江-杭州':
        area = 138
    if place == '浙江-丽水':
        area = 134
    if place == '浙江-金华':
        area = 135
    if place == '浙江-温州':
        area = 149
    if place == '浙江-台州':
        area = 287
    if place == '浙江-衢州':
        area = 288
    if place == '浙江-宁波':
        area = 289
    if place == '浙江-绍兴':
        area = 303
    if place == '浙江-嘉兴':
        area = 304
    if place == '浙江-湖州':
        area = 305
    if place == '浙江-舟山':
        area = 306
    return area


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
    n, i, a, result = list( t ), list( e ), {}, []
    ln = int( len( n ) / 2 )
    start, end = n[ln:], n[:ln]
    a = dict( zip( end, start ) )
    return "".join( [a[j] for j in e] )


def get_ptbk(uniqid: str, cookie: str) -> str:
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Host": "index.baidu.com",
        "Referer": "http://index.baidu.com/v2/main/index.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    session = requests.Session()
    session.headers.update( headers )
    with session.get(
            url=f"http://index.baidu.com/Interface/ptbk?uniqid={uniqid}"
    ) as response:
        ptbk = response.json()["data"]
        return ptbk


def baidu_info_index(word, start_date, end_date, place, cookie):
    # 百度资讯指数
    global area
    area = cityzh( place )
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Cookie": cookie,
            "Host": "index.baidu.com",
            "Referer": "http://index.baidu.com/v2/main/index.html",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
        }
        w = '{"name":"%s","wordType":1}' % word
        url = 'http://index.baidu.com/api/FeedSearchApi/getFeedIndex?area=%d&word=[[%s]]&startDate=%s&endDate=%s' % (
            area, w, start_date, end_date)
        r = requests.get( url=url, headers=headers )
        data = r.json()["data"]
        all_data = data["index"][0]["data"]
        uniqid = data["uniqid"]
        ptbk = get_ptbk( uniqid, cookie )
        result = decrypt( ptbk, all_data ).split( "," )
        result = [int( item ) if item != "" else 0 for item in result]
        temp_df_7 = pd.DataFrame(
            [pd.date_range( start=start_date, end=end_date ), result],
            index=["date","data"],
        ).T
        #temp_df_7.index =pd.to_datetime( temp_df_7["date"] )
        #del temp_df_7["date"]
        pd.set_option( 'display.max_rows', None )
        return temp_df_7
    except:
        return None


if __name__ == "__main__":
    cookie='BIDUPSID=AA6ACB40BA91D8400799425B2165C78C; PSTM=1589373008; __yjs_duid=1_6f7a9a5697f1f46c538f72dd1522fbef1620059845652; BAIDUID=1421E8B162973B856BE738DAF923D17D:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ai-studio-ticket=6B753BD18F854EDD8776310B1518A8B7C7921533AAAE433B94A5A713F35F5101; BAIDUID_BFESS=1421E8B162973B856BE738DAF923D17D:FG=1; BDRCVFR[8gzLr2xelNt]=mk3SLVN4HKm; delPer=0; PSINO=2; H_PS_PSSID=34099_33967_34004_34072_34092_34111_26350_34244; BA_HECTOR=a48ka40g8h258g85e11gf4t2j0r; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1626419421,1626448054,1626502229,1626502433; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1626502447; BDUSS=nhhSTFUUG9IclphYX5sYjdpdm1qUThtQThYZDhyTm44U3RteUlhOURmWUhBeHBoRUFBQUFBJCQAAAAAAQAAAAEAAAD0TnIA8LDO9eihAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd28mAHdvJgY; BDUSS_BFESS=nhhSTFUUG9IclphYX5sYjdpdm1qUThtQThYZDhyTm44U3RteUlhOURmWUhBeHBoRUFBQUFBJCQAAAAAAQAAAAEAAAD0TnIA8LDO9eihAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd28mAHdvJgY; ab_sr=1.0.1_MDAxYjM5MTU2OGMxNTIzNmJlNDc1NWJkOTFmZDkxM2U4NjM4YmRhMzQzN2JmZDA3YzdjODE5N2I0ZDgwMDY0ZmFmZDFiM2ZhNTJjMDU0N2RkYzg5OTRjNjc5NjM0MzExNGUxNjU4YmQ5MTQ4NjQyNGI1YzRlYTc2YWRlMzM1OTY3ZmY3ZTE0NDA4M2E3ZGEyNzYzMTYzOGQ2Yjk2ZGEzYg==; __yjs_st=2_ZmFiNTY2ZWIwOWNlYTczYjliM2M4YjQ5OTNhMzM3YzgzNzY3NzdlNTVhODgwZWUyMGNkNzA4MDAzZDRjYjgwMGYxZjc5Zjc0NTk2NTljOGM2OWM1ZmFjZjRlN2M4NzIwYmNlYjMzZjQ4YmE4MWE3MDUwZGFkY2Y1ODY2MTZlNTY5Yjc1NTI2MjVkNjRiYjVkYjA1MzhlODc5ZjhjNjFkNWJjYjc3MGI1YzI1NGRmNGE2ZmNhMjY0ZTJlMDlmNGNlOTlkZTA4MzZmZTliYzIwYjFlOWI1Nzk1ZTVmZDFhYjAwOWFjZWUxODM1YTM3NDU2ZmJhOWEzZDk1ZWRlM2RiNF83Xzc4Yzg0YmQw; RT="z=1&dm=baidu.com&si=qjvtrzlnmeo&ss=kr7dfjty&sl=j&tt=b8d&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4por&ul=9dwv'
    shuju = {}
    place_list = {'全国', '安徽', '澳门', '北京', '重庆', '福建', '广东', '广西', '甘肃', '贵州', '河北', '黑龙江', '河南', '湖南', '湖北', '海南', '吉林',
                  '江苏', '江西', '辽宁', '内蒙古', '宁夏', '青海', '上海', '四川', '山东', '山西', '陕西', '天津', '台湾', '西藏', '香港', '新疆', '云南',
                  '浙江', '安徽-合肥', '安徽-铜陵', '安徽-黄山', '安徽-池州', '安徽-宣城', '安徽-巢湖', '安徽-淮南', '安徽-宿州', '安徽-六安', '安徽-滁州',
                  '安徽-淮北', '安徽-阜阳', '安徽-马鞍山', '安徽-安庆', '安徽-蚌埠', '安徽-芜湖', '安徽-亳州', '福建-福州', '福建-莆田', '福建-三明', '福建-龙岩',
                  '福建-厦门', '福建-泉州', '福建-漳州', '福建-宁德', '福建-南平', '广东-广州', '广东-深圳', '广东-东莞', '广东-云浮', '广东-佛山', '广东-湛江',
                  '广东-江门', '广东-惠州', '广东-珠海', '广东-韶关', '广东-阳江', '广东-茂名', '广东-潮州', '广东-揭阳', '广东-中山', '广东-清远', '广东-肇庆',
                  '广东-河源', '广东-梅州', '广东-汕头', '广东-汕尾', '广西-南宁', '广西-柳州', '广西-桂林', '广西-贺州','广西-贵港', '广西-玉林', '广西-河池',
                  '广西-北海', '广西-钦州', '广西-防城港', '广西-百色', '广西-梧州', '广西-来宾', '广西-崇左', '甘肃-兰州', '甘肃-庆阳', '甘肃-定西', '甘肃-武威',
                  '甘肃-酒泉', '甘肃-张掖', '甘肃-嘉峪关', '甘肃-平凉', '甘肃-天水', '甘肃-白银', '甘肃-金昌', '甘肃-陇南', '甘肃-临夏', '甘肃-甘南', '贵州-贵阳',
                  '贵州-黔南', '贵州-六盘水', '贵州-遵义', '贵州-黔东南', '贵州-铜仁', '贵州-安顺', '贵州-毕节','贵州-黔西南', '河北-石家庄', '河北-衡水', '河北-张家口',
                  '河北-承德', '河北-秦皇岛', '河北-廊坊', '河北-沧州', '河北-保定', '河北-唐山', '河北-邯郸', '河北-邢台', '黑龙江-哈尔滨', '黑龙江-大庆',
                  '黑龙江-伊春', '黑龙江-大兴安岭', '黑龙江-黑河', '黑龙江-鹤岗', '黑龙江-七台河', '黑龙江-齐齐哈尔', '黑龙江-佳木斯', '黑龙江-牡丹江', '黑龙江-鸡西',
                  '黑龙江-绥化', '黑龙江-双鸭山', '河南-郑州', '河南-南阳', '河南-新乡', '河南-开封', '河南-焦作', '河南-平顶山', '河南-许昌', '河南-安阳',
                  '河南-驻马店', '河南-信阳', '河南-鹤壁', '河南-周口', '河南-商丘', '河南-洛阳', '河南-漯河', '河南-濮阳', '河南-三门峡', '河南-济源', '湖南-长沙',
                  '湖南-岳阳', '湖南-衡阳', '湖南-株洲', '湖南-湘潭', '湖南-益阳', '湖南-郴州','湖南-湘西', '湖南-娄底', '湖南-怀化', '湖南-常德', '湖南-张家界',
                  '湖南-永州', '湖南-邵阳','湖北-武汉', '湖北-黄石', '湖北-荆州', '湖北-襄阳', '湖北-黄冈', '湖北-荆门', '湖北-宜昌', '湖北-十堰', '湖北-随州', "湖北-恩施", '湖北-鄂州',
                  '湖北-咸宁', '湖北-孝感', '湖北-仙桃', '湖北-天门', '湖北-潜江', '湖北-神农架', '海南-海口', '海南-万宁', '海南-琼海', '海南-三亚', '海南-儋州',
                  '海南-东方', '海南-五指山', '海南-文昌', '海南-陵水', '海南-澄迈', '海南-乐东', '海南-临高', '海南-定安', '海南-昌江', '海南-屯昌', '海南-保亭',
                  '海南-白沙', '海南-琼中', '吉林-长春', '吉林-四平', '吉林-辽源', '吉林-松原', '吉林-吉林', '吉林-通化', '吉林-白山', '吉林-白城', '吉林-延边',
                  '江苏-南京', '江苏-苏州', '江苏-无锡', '江苏-连云港', '江苏-淮安', '江苏-扬州', '江苏-泰州', '江苏-盐城', '江苏-徐州', '江苏-常州', '江苏-南通',
                  '江苏-镇江', '江苏-宿迁', '江西-南昌', '江西-九江', '江西-鹰潭', '江西-抚州', '江西-上饶', '江西-赣州', '江西-吉安', '江西-萍乡', '江西-景德镇',
                  '江西-新余', '江西-宜春', '辽宁', '辽宁-沈阳', '辽宁-大连', '辽宁-盘锦', '辽宁-鞍山', '辽宁-朝阳', '辽宁-锦州', '辽宁-铁岭', '辽宁-丹东',
                  '辽宁-本溪', '辽宁-营口', '辽宁-抚顺', '辽宁-阜新', '辽宁-辽阳', '辽宁-葫芦岛', '内蒙古-呼和浩特', '内蒙古-包头', '内蒙古-鄂尔多斯', '内蒙古-巴彦淖尔',
                  '内蒙古-乌海', '内蒙古-阿拉善盟', '内蒙古-锡林郭勒盟', '内蒙古-赤峰', '内蒙古-通辽', '内蒙古-呼伦贝尔', '内蒙古-乌兰察布', '内蒙古-兴安盟', '宁夏-银川',
                  '宁夏-吴忠', '宁夏-固原', '宁夏-石嘴山', '宁夏-中卫', '青海-西宁', '青海-海西', '青海-海东', '青海-玉树', '青海-海南', '青海-海北', '青海-黄南',
                  '青海-果洛', '四川-成都', '四川-宜宾', '四川-绵阳', '四川-广元', '四川-遂宁', '四川-巴中', '四川-内江', '四川-泸州', '四川-南充', '四川-德阳',
                  '四川-乐山', '四川-广安', '四川-资阳', '四川-自贡', '四川-攀枝花', '四川-达州', '四川-雅安', '四川-眉山', '四川-甘孜', '四川-阿坝', '四川-凉山',
                  '山东-济南', '山东-滨州', '山东-青岛', '山东-烟台', '山东-临沂', '山东-潍坊', '山东-淄博', '山东-东营', '山东-聊城', '山东-菏泽', '山东-枣庄',
                  '山东-德州', '山东-威海', '山东-济宁', '山东-泰安', '山东-莱芜', '山东-日照', '山西-太原', '山西-大同', '山西-长治', '山西-忻州', '山西-晋中',
                  '山西-临汾', '山西-运城', '山西-晋城', '山西-朔州', '山西-阳泉', '山西-吕梁', '陕西-西安', '陕西-铜川', '陕西-安康', '陕西-宝鸡', '陕西-商洛',
                  '陕西-渭南', '陕西-汉中', '陕西-咸阳', '陕西-榆林','陕西-延安', '西藏-拉萨', '西藏-日喀则', '西藏-那曲', '西藏-林芝', '西藏-山南', '西藏-昌都', '西藏-阿里', '新疆-乌鲁木齐', '新疆-石河子',
                  '新疆-吐鲁番', '新疆-昌吉', '新疆-哈密', '新疆-阿克苏', '新疆-克拉玛依', '新疆-博尔塔拉', '新疆-阿勒泰', '新疆-喀什', '新疆-和田', '新疆-巴音郭楞',
                  '新疆-伊犁', '新疆-塔城', '新疆-克孜勒苏柯尔克孜', '新疆-五家渠', '新疆-阿拉尔', '新疆-图木舒克', '云南-昆明', '云南-玉溪', '云南-楚雄', '云南-大理',
                  '云南-昭通', '云南-红河', '云南-曲靖', '云南-丽江', '云南-临沧', '云南-文山', '云南-保山', '云南-普洱', '云南-西双版纳', '云南-德宏', '云南-怒江',
                  '云南-迪庆', '浙江-杭州', '浙江-丽水', '浙江-金华', '浙江-温州', '浙江-台州', '浙江-衢州', '浙江-宁波', '浙江-绍兴', '浙江-嘉兴', '浙江-湖州',
                  '浙江-舟山'}
    for p in place_list:
        shuju[p] = baidu_info_index( "觉醒年代", '2021-02-01', '2021-07-15', p, cookie )
        fileName = 'info' + p + '.csv'
        with open( fileName, 'w', encoding='utf-8' ) as f:
            f.write( str( shuju[p] ) )
            print( "保存了%s的csv文件" %p)
    print("保存完毕")
