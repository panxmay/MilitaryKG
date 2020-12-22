from WeiPin.tools.html_paser import html_paser
import re

url_list = []

# 首页
def get_homepage():
    url = "https://mil.news.sina.com.cn/"
    html = html_paser(url, 'utf-8')
    if html == 0:
        print('主页出错')
        exit()

    pattern = re.compile('"(https://mil.news.sina.com.cn/[^"]+)"')
    url_list.extend(re.findall(pattern, html))
    print(len(url_list))
    return url_list


# 国际
def get_world():
    url_pre = "http://mil.news.sina.com.cn/roll/index.d.html?cid=57919&page="
    for i in range(1,6):
        html = html_paser(url_pre+str(i), 'utf-8')
        if html == 0:
            print('主页出错')
            exit()

        pattern = re.compile('"(https://mil.news.sina.com.cn/[^"]+)"')
        url_list.extend(re.findall(pattern, html))
    print(len(url_list))
    return url_list


# 中国
def get_china():
    url_pre = "http://mil.news.sina.com.cn/roll/index.d.html?cid=57918&page="
    for i in range(1,6):
        html = html_paser(url_pre+str(i), 'utf-8')
        if html == 0:
            print('主页出错')
            exit()

        pattern = re.compile('"(https://mil.news.sina.com.cn/[^"]+)"')
        url_list.extend(re.findall(pattern, html))
    print(len(url_list))
    return url_list
