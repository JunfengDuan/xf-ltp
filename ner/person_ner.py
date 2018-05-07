# coding:utf-8
from ner.cn_ner import *
from ner.sxr_ner import *


def name_count(text, lexicon_path):

    text = text.replace('\n', '')
    entity = text_ner(text, lexicon_path)
    persons = lxr_extract(entity)

    _, sx_persons = sxr_ner(text)

    for name in persons:
        if name in sx_persons:
            persons.remove(name)

    count = int(len(persons))
    return str(dict(result=count))
