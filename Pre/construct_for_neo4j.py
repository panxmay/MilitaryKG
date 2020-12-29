import csv
import pandas as pd


def list_to_rdf(title):
    save_path = '../data/' + title + '_rdf.txt'
    path = '../data/triples/' + title + '.txt'
    fw = open(save_path, 'w+', encoding='utf-8')
    for line in open(path, 'r+', encoding='utf-8'):
        temp = line.strip()[1:-1].replace("'", '').split(',')
        if len(temp) < 3:
            continue
        gap_str = ';;;;;'
        fw.write(temp[0] + gap_str + temp[1] + gap_str + temp[2] + '\n')
    fw.close()

def clean_chr(title):
    fixs = ['','_property']
    for fix in fixs:
        writes = set()
        path = '../data/import_neo4j/source/' + title + fix+'.txt'
        for line in open(path, 'r+', encoding='utf-8'):
            writes.add(line.strip().replace('&nbsp;',''))
        fw = open(path, 'w+', encoding='utf-8')
        for item in writes:
            fw.write(item+'\n')
        fw.close()

# 转存为CSV文件，并添加id
def to_csv(title):
    path = '../data/import_neo4j/source/' + title + '.txt'
    save_path = '../data/import_neo4j/' + title + '.txt'
    temp = []
    for line in open(path,'r',encoding='utf-8'):
        temp.append(line.strip())
    df = pd.DataFrame(temp,columns=[title])
    df.to_csv(save_path, index=True, sep=',')



def get_all_property(title):
    property_set = set()
    path = '../data/import_neo4j/source/'+title+'_property.txt'
    for line in open(path,'r',encoding='utf-8'):
        temp = line.strip().split(';;;;;')
        if len(temp)<3:
            continue
        property_set.add(temp[1])
    return property_set

def give_id():
    pass

def run():
    titles = ["War", "Weapon", "Company", "Person", "Country"]
    for item in titles:
        # clean_chr(item)
        # print(item, get_all_property(item))
        # list_to_rdf(item)
        to_csv(item)

if __name__ == '__main__':
    run()
