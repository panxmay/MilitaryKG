from MilitaryKG.tools.html_paser import html_paser
from bs4 import BeautifulSoup as bs
from MilitaryKG.tools.IO_file import write_to_txt
import re


def get_weapons():
    weapons = []
    gap_str = ';;;;;'
    for i in range(0, 112):
        url = "http://weapon.huanqiu.com/weaponlist/aircraft/list_0_0_0_0_"
        html = html_paser(url + str(i), 'utf-8')
        if html == 0:
            print('页面出错')
            exit()
        soup = bs(html, 'html.parser')
        div = soup.find(attrs={"class":'picList'})
        if div is None:
            continue
        lis = div.findAll('li')
        for item in lis:
            name_span = item.find(attrs={"class": 'name'})
            if name_span is None:
                continue
            name = name_span.text
            category_span = item.find(attrs={"class": 'category'})
            category = '-1'
            if category_span is not None:
                category = category_span.text
            weapons.append(name + gap_str + 'category' + gap_str + category)
    return weapons


path = '../../data/news/weapons.txt'
weapons = get_weapons()
with open(path,'w+',encoding='utf-8') as fw:
    for item in weapons:
        fw.write(item+'\n')



