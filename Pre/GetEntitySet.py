import csv
import os

pypath = '/data/gaochaoyu/xmay/pyProjects/'
source_path = os.path.abspath(pypath+'MilitaryKG/data/entity/entity.txt')


entity_set =  set()
for item in open(source_path,'r',encoding='utf-8'):
    entity_set.add(item.strip())

