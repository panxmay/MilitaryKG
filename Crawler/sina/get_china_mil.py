from bs4 import BeautifulSoup as bs
import pandas as pd
from queue import Queue
import datetime
import re
from MilitaryKG.tools.html_paser import html_paser
from MilitaryKG.tools.MyThreadPool import MyThreadPool
from MilitaryKG.Crawler.sina.get_urls import get_homepage

class Producer(object):
    @staticmethod
    def producer(q, data):
        q.put(data)

def insertDB(data):
    fp.write(str(data)+'\n')
    fp.flush()

# 构造生产者
def product_data():
    entity_queue = Queue()
    for item in g:
        Producer.producer(entity_queue, item)
    return entity_queue

# 爬取每一个页面
def turn_page_thread(submission):
    html = html_paser(submission, 'utf-8')
    if html == 0:
        return
    soup = bs(html, 'html.parser')
    main_title = soup.find(attrs={"class":'main-title'})
    if main_title is None:
        return
    title = main_title.text
    category_box = soup.find(attrs={'class': 'article'})
    if category_box is None:
        return
    categories = category_box.findAll('p')
    article = ''
    if len(categories)==0:
        return
    for item in categories:
        article +=item.text
    Producer.producer(entity_queue, (title, article))

maxsize = 1

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
save_path = "../../data/news/sina.txt"
fp = open(save_path,'w+',encoding='utf-8')

q = product_data()
entity_queue = Queue()
pool = MyThreadPool()
pool.addthread(queue=q, size=maxsize, func=turn_page_thread, timeout=15)
pool.addthread(queue=entity_queue, size=1, func=insertDB, timeout=20)
pool.startAll()
pool.joinAll()
fp.close()

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "结束")

