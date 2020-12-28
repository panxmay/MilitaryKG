

def del_blank_line(file_name):
    rows = []
    for line in open(file_name,'r',encoding='utf-8'):
        if line=='\n':
            continue
        rows.append(line)
    with open(file_name,'w+',encoding='utf-8') as fw:
        for row in rows:
            fw.write(row)



# del_blank_line('../data/entity/war.txt')
# del_blank_line('../data/entity/company.txt')
del_blank_line('../data/triples/company.txt')