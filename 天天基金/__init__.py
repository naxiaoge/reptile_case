
import requests
import re
import csv
"""
数据位置：
    http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2020-12-19&ed=2021-12-19&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.615248591565194
代码实现：
    1. 发送请求
        
    2.获取数据
    3.解析数据
    4.保存数据
    5.多页爬虫

"""
# 选中替换内容
# CTRL+R
# 第一个框中 (.*?):(.*)
# 第二个框中 '$1':'$2',
# 点亮星星
headers = {
        'Cookie': 'qgqp_b_id=7b2c433bb45d6eb82e21a6c0d6398056;_adsame_fullscreen_16928=1;st_si=65917890133347;st_asi=delete;st_pvi=40778661279695;st_sp=2021-12-16%2020%3A28%3A30;st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink;st_sn=2;ASP.NET_SessionId=c3aiuxgxmzn2r3azfw0hb4du;st_psi=20211219104226195-112200312936-5089623460',
        'Host': 'fund.eastmoney.com',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://fund.eastmoney.com/data/fundranking.html',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/96.0.4664.110Safari/537.36',
    }
# url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2020-12-16&ed=2021-12-16&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.6459658521075855'

for page in range(1, 193):
    print(f'==================正在爬取第{page}页========================')
    url = f'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=6yzf&st=desc&sd=2020-12-16&ed=2021-12-16&qdii=&tabSubtype=,,,,,&pi={page}&pn=50&dx=1&v=0.6459658521075855'


    # 1.发送请求
    response = requests.get(url=url, headers=headers)
    # 2.获取数据
    data = response.text
    # 3.解析数据 筛选数据
    # re
    # 第一个参数 正则表达式语法 第二个参数我们需要在哪里匹配
    data_str = re.findall('\[(.*?)\]', data)[0]
    # 4.保存数据
    # 表格当中
    # 数据类型转换
    # 列表 元组
    # eval 可以帮助我们把字符串转换为 列表/字典/元组/整数类型/Boolean/浮点类型...
    tuple_data = eval(data_str)

    for td in tuple_data:
        # 把td转换成列表
        td_list = td.split(',')
        # 保存数据
        with open('天天基金.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(td_list)
        print(td)
