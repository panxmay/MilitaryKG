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
    source_path = '../../data/entity/War.txt'

    entity_set = set()
    for item in open(source_path, 'r', encoding='utf-8'):
        entity_set.add(item.strip())
    return entity_set

def GetCompanySet():
    entity_set = set()
    source_path = '../../data/entity/Company.txt'

    entity_set = set()
    for item in open(source_path, 'r', encoding='utf-8'):
        entity_set.add(item.strip())
    return entity_set

def GetWeaponSet():
    entity_set = set()
    source_path = '../../data/entity/Weapon.txt'

    entity_set = set()
    for item in open(source_path, 'r', encoding='utf-8'):
        entity_set.add(item.strip())
    return entity_set

# GetWeaponSet()
