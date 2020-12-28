import csv
import os

def GetEntity():
    pypath = '/data/gaochaoyu/xmay/pyProjects/'
    source_path = os.path.abspath(pypath + 'MilitaryKG/data/entity/entity.txt')

    entity_set = set()
    for item in open(source_path, 'r', encoding='utf-8'):
        entity_set.add(item.strip())
    return entity_set

def GetWarSet():
    entity_set = set()
    source_path = '../../data/entity/war.txt'

    entity_set = set()
    for item in open(source_path, 'r', encoding='utf-8'):
        entity_set.add(item.strip())
    return entity_set

def GetCompanySet():
    entity_set = set()
    source_path = '../../data/entity/company.txt'

    entity_set = set()
    for item in open(source_path, 'r', encoding='utf-8'):
        entity_set.add(item.strip())
    return entity_set

def GetWeaponSet():
    entity_set = set()
    source_path = '../data/triples/weapon_rdf.txt'

    entity_set = set()
    for item in open(source_path, 'r', encoding='utf-8'):
        templist = item.strip().split(';;;;;')
        if len(templist)<2:
            continue
        entity_set.add(templist[0])
    with open('../data/entity/Weapon.txt','w+',encoding='utf-8') as fw:
        for item in entity_set:
            fw.write(item+'\n')
    return entity_set

GetWeaponSet()
