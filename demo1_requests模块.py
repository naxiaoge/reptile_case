import requests, re

# url="http://httpbin.org/get"
# url="https://www.woyaogexing.com"
# r=requests.get(url)
# print(r) #返回
# print(type(r))

# r.text 获得返回值里面的源代码 ※
# print(r.text)

# r.content 获取返回值的源代码的二进制码 decode(使用哪种编码解析) 解码
# 正常情况,我们会使用text,如果出现了乱码,先用content然后.decode()
# print(r.content.decode('utf-8'))

# r.encoding 获得返回值的编码
# print(r.encoding)

# r.status_code 返回http状态码
# 1** 正在请求
# 2** 请求成功
# 3** 网页跳转重定向
# 4** 请求的资源错误
# 5** 服务器错误
# print(r.status_code)


# cookies示例
# r.cookies 返回网页中的cookie
# 1.从登陆页面dologin 获取cookie 保存下来
# 2.再次请求其他的网页的时候,带上cookie
login_url="http://www.antvv.com/login/dologin.php"
# # data  请求的时候带的表单内容
# login_r=requests.post(login_url,data={"uname":"admin","upwd":"123456"})
# login_cookie=login_r.cookies
#
# # cookies 请求的时候附带的cookie
url="http://www.antvv.com/login/index.php"
# # r=requests.get(url,cookies=login_cookie)
# # print(r.text)


# 使用requests模块中的session 模拟浏览器
# s=requests.session() # 模拟了一个浏览器
# # 登陆的时候获取到的cookie会自动的保存到s中
# s.post(login_url,data={"uname":"admin","upwd":"123456"})
# # 后面再使用s.get() 会自动带上cookie
# r=s.get(url)
# print(r.text)


# data  请求的时候带的表单内容
# cookie 请求时候带的cookie
# headers 请求的时候的消息头

# 解决UA问题,加上headers参数
# url="https://www.zhihu.com/explore"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.132 Safari/537.36"
}
# r=requests.get(url,headers=headers)
# print(r.text)

# 返回回来的结果类似 Python中的字典,能否使用? 可以的,使用r.json()转换成字典或者列表
# 给get方式传值
# 1. 使用params传参
# url="http://httpbin.org/get"
# params={
#     "login_status":1,
#     "uname":"admin",
#     "upwd":"123456"
# }
# r=requests.get(url,headers=headers,params=params)
# 2.直接拼接url
# url="http://httpbin.org/get?uname=admin&upwd=123456&login_status=1"
# r=requests.get(url,headers=headers)
# # print(r.text)
# # print(type(r.text))
# resp_dict=r.json()
# print(resp_dict)
# print(type(resp_dict))
# print(resp_dict['origin'])


# 设置代理 proxies
# url="http://httpbin.org/get?uname=admin&upwd=123456&login_status=1"
# proxies={
#     "http":"58.243.50.184:53281",
# }
# r=requests.get(url,headers=headers,proxies=proxies)
# print(r.text) # 58.33.141.61, 58.33.141.61
# 使用了高匿代理之后 112.85.166.240, 112.85.166.240
# 透明代理 58.33.141.61, 58.243.50.184, 58.33.141.61

# 证书验证  verify
# url="https://www.12306.cn/index/"
# r=requests.get(url,headers=headers,verify=False)
# print(r.text)

# 请求图片,资源,下载 stream=True 流式传输
# url="https://www.12306.cn/index/images/abanner03.jpg"
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.132 Safari/537.36"
# }
# r=requests.get(url,headers=headers,stream=True)
# # 使用r.iter_content(size) 从流中每次读取一部分
# with open("./12306.png",'wb') as file:
#     for j in r.iter_content(1024):
#         file.write(j)
        # 10分钟时间练习一下, 请求下载资源文件,代理访问,基本get访问

# 批量下载资源文件

# woyaogexing_url="https://www.woyaogexing.com/touxiang/"
# r=requests.get(woyaogexing_url,headers=headers)
# html=r.content.decode('utf-8')
# # print(type(html))
# # <img class="lazy" src="//img2.woyaogexing.com/2019/05/11/8f69c2d8651d4d7db8c544c6d1998e4a!400x400.jpeg" width="180" height="180" />
# # <img class="lazy" src="//img2.woyaogexing.com/2019/05/11/c64e26fb02b540599c972d89ee20e87d!400x400.jpeg" width="180" height="180" />
# # 设置正则表达式
# regx=re.compile('<img class="lazy" src="(.*?)" width="180" height="180" />')
# # 使用正则匹配html中所有满足条件的内容 findall() 查找所有
# img_list=regx.findall(html)
# # 拼接成全路径
# img_list=list(map(lambda x:"https:"+x,img_list))
# num=1
# for once_img in img_list:
#     img_r=requests.get(once_img,headers=headers,stream=True)
#     with open("./images/%d.jpg"%num,'wb') as file:
#         for j in img_r.iter_content(1024):
#             file.write(j)
#     print("%d个图片下载成功"%num)
#     num+=1
    # 课间休息 :15上课,先练习一下

# 上传文件 files={}

# url="http://httpbin.org/post"
# fp=open("a.txt",'r')
# img_fp=open("12306.png",'rb')
# # 上传文件的时候,不需要read出来,直接传文件的资源
# files={
#     "file":fp,
#     'img':img_fp
# }
# r=requests.post(url,files=files)
# print(r.text)


