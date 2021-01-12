import datetime
from bs4 import BeautifulSoup as bs
from MilitaryKG.tools.html_paser import html_paser
import json

def read_txt_set(path):
    en_set = set()
    for line in open(path,'r',encoding='utf-8'):
        en_set.add(line.strip())
        page_set[line.strip()] = set()
        subcat_set[line.strip()] = set()
    return en_set

# 爬取每一个页面
def crawler(concept):
    global cur_level_entity
    url_pre = "https://zh.wikipedia.org/wiki/Category:"
    url = url_pre+concept
    html = html_paser(url, 'utf-8')
    if html == 0:
        return
    # fine page

    soup = bs(html, 'html.parser')
    pages = soup.find(attrs={'id': 'mw-pages'})
    if pages is not None:
        links = pages.findAll('a')
        for link in links:
            page_set[concept].add(link.text)
            if link.text not in entity_set:
                entity_set.add(link.text)

    subconcepts = soup.find(attrs={'id': 'mw-subcategories'})
    if subconcepts is not None:
        links = subconcepts.findAll('a')
        for link in links:
            subcat_set[concept].add(link.text)
            if link.text not in con_set:
                cur_level_entity.add(link.text)
                con_set.add(link.text)

def write_to_txt(source_path, data):
    fw = open(source_path,'w+',encoding='utf-8')
    for item in data:
        fw.write(item+'\n')
    fw.close()

def innitial(i):
    entity_path = '../../data/ontology/entity'+str(i)+'.txt'
    en_set = read_txt_set(entity_path)
    return en_set

def run():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    global cur_level_entity
    for i in range(1,6):
        en_set = innitial(i)
        for en in en_set:
            crawler(en)
        write_to_txt('../../data/ontology/entity' + str(i+1) + '.txt',cur_level_entity)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        cur_level_entity = set()
    write_to_txt('../../data/ontology/entity.txt',entity_set)
    write_to_txt('../../data/ontology/concept.txt',con_set)
    write_to_txt('../../data/ontology/pages.txt',page_set)
    write_to_txt('../../data/ontology/subcategory.txt',subcat_set)


page_set = {}
subcat_set = {}
con_set = set()
entity_set = set()
cur_level_entity = set()
run()



