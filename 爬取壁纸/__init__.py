import json
import re
import requests

url = "http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=1&pageSize=50&nodeId=21089"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
r = requests.get(url, headers=headers)
# print(r.content.decode('utf-8'))
resp_str = r.json()
resp_dict = json.loads(resp_str)
# print(resp_dict)
# print(type(resp_dict))
# print(resp_dict['totalCount'])

for once in resp_dict['body']:
    # print(once)
    img_url = once['originImg']
    img_name = once['title'][1:-5]
    # img_name=img_name.replace("/",'').replace("\\","").replace("|","").replace("\"","").replace("?","").replace(">","").replace("<","").replace("*","").replace(":","")
    img_name = re.sub("[/\\\\|\?\*:><\"]", '', img_name)
    # print(img_url,img_name)
    img_r = requests.get(img_url, headers=headers, stream=True)
    with open("./images/%s.jpg" % img_name, 'wb') as file:
        for j in img_r.iter_content(10240):
            file.write(j)
    print("%s.jpg下载成功" % img_name)

