# coding:utf-8
import os

from ner import element_extract as extract


# 读文件
def read_file(path):
    with open(path, 'rt', encoding='utf-8') as f:
        data = f.read()
    return data


# 加载受信人列表
def read_sxr(sxr_file):
    sxr_file_path = os.path.join('dict', sxr_file)
    person = []
    with open(sxr_file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.replace('\n', '').replace(' ', '')
            person.append(line)
    return person


# 加载受信人关联关系列表
def read_sxr_rel(sxr_file):
    sxr_file_path = os.path.join('dict', sxr_file)
    person_rel_dict = dict()
    person_rel_list = []
    with open(sxr_file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            name_short = line.split(':')
            person_rel_dict[name_short[0]] = name_short[1].split(' ')
            full_name = [name_short[0]]
            full_name.extend(name_short[1].split(' '))
            person_rel_list.append(full_name)
    return person_rel_dict, person_rel_list


# 分词
def only_seg(sentence, lexicon_path=None):
    text = sentence.replace('\n', '')
    segs = list(extract.segment(text, lexicon_path))
    return str(dict(result=segs))


# 实体抽取
# sentence='尊敬的习大大您好'
def text_ner(sentence, lexicon_path=None):
    word = extract.segment(sentence, lexicon_path)
    pos = extract.pos(word)
    ner = extract.ner(word, pos)
    entity = list(zip(list(word), list(pos), list(ner)))
    return entity


# 受信对象抽取
# entities=[('尊敬', 'v', 'O'), ('的', 'u', 'O'), ('习大大', 'nh', 'S-Nh'), ('您好', 'i', 'O')]
def sx_object_extract(entity):
    labels = ['S-Nh', 'S-Ni']
    pos = ['n', 'ni', 'nh', 'ns', 'nl', 'j']
    sx_object = []
    for n in entity:
        if n[2] in labels or n[1] in pos or n[0] == '投诉办':
            if n[0] not in sx_object:
                sx_object.append(n[0])
    return sx_object


# 来信人抽取
# entities=[('我', 'r', 'O'), ('叫', 'v', 'O'), ('曾晓敏', 'nh', 'S-Nh')]
def lxr_extract(entity):
    labels = ['S-Nh']
    pos = ['nh']
    lxr = []
    for n in entity:
        if n[2] in labels or n[1] in pos:
            if len(n[0]) > 1 and n[0] not in lxr:
                lxr.append(n[0])
    return lxr


# 抽取文本的第一句和最后一句
def get_effect_sent(text):

    sentences = extract.split(text)
    # print('sentences:', sentences)
    effective_sents = [sentences[0], sentences[-1]]
    if len(sentences) > 1:
        cadidate_sents = sentences[1]

    return effective_sents, cadidate_sents


# 组织机构抽取
def org_extract(entity):
    labels = []
    pos = ['ni']
    org = []
    for n in entity:
        if n[2] in labels or n[1] in pos:
            if len(n[0]) > 1 and n[0] not in org:
                org.append(n[0])
    return org


# 地址抽取
def address_extract(entity):
    labels = ['B-Ns', 'I-Ns', 'E-Ns', 'S-Ns']
    pos = ['ns']
    address = []
    s = ''
    for n in entity:
        if n[1] in pos or n[2] in labels:
            s += n[0]
            continue
        else:
            if s != "" and s not in address:
                address.append(s)
            s = ''
    return address


if __name__ == '__main__':

    file_path = '/home/jfd/Documents/信访/数据/史主任发来103个案例(20180223)/2017022857760.txt'
    doc = read_file(file_path)
    sents = get_effect_sent(doc)
    text_sx = []
    for t in sents:
        entities = text_ner(t)
        sx_objects = sx_object_extract(entities)
        sent_object = (t, sx_objects)
        text_sx.append(sent_object)
    for x in text_sx:
        print(x)



