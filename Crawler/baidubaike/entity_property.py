from bs4 import BeautifulSoup as bs
import pandas as pd
from queue import Queue
import datetime
import re
from MilitaryKG.tools.html_paser import html_paser
from MilitaryKG.tools.MyThreadPool import MyThreadPool
from MilitaryKG.Pre.GetEntitySet import GetEntity,GetWarSet,GetCompanySet
class Producer(object):
    @staticmethod
    def producer(q, data):
        q.put(data)

def insertDB(data):
    fp.write(str(data)+'\n')
    fp.flush()

# 构造生产者
def product_data(title):
    entity_queue = Queue()
    eval_str = 'Get'+title+'Set()'
    entity_set = eval(eval_str)
    for item in entity_set:
        Producer.producer(entity_queue, item)
    return entity_queue

def insertDB(sql_value):
    fp.write(str(sql_value)+'\n')
    fp.flush()

# 爬取每一个页面
def turn_page_thread(submission):
    url_pre = "https://baike.baidu.com/item/"
    url = url_pre+submission
    html = html_paser(url, 'utf-8')
    if html == 0:
        return
    pattern = re.compile('<dt class="basicInfo-item name">\s*([^<]+)\s*</dt>\s*<dd class="basicInfo-item value">\s*([^<]+)\s+</dd>')
    triples = re.findall(pattern, html)
    if len(triples) == 0:
        return 
    for item in triples:
        triple = [submission, item[0], item[1]]
        Producer.producer(entity_queue, triple)

maxsize = 25

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# save_path = "../../data/baidubaike/property.txt"
title = ['War','Company','Entity']
save_path = '../../data/triples/'+title[0]+'.txt'
fp = open(save_path,'w+',encoding='utf-8')

q = product_data(title[0])
entity_queue = Queue()
pool = MyThreadPool()
pool.addthread(queue=q, size=maxsize, func=turn_page_thread, timeout=15)
pool.addthread(queue=entity_queue, size=1, func=insertDB, timeout=20)
pool.startAll()
pool.joinAll()
fp.close()

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "结束")
