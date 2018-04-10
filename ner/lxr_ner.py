# coding:utf-8
from ner.cn_ner import *

sxr = read_sxr('sxr.txt')


def lxr_ner(text):

    text = text.replace('\n', '')
    sentences, cad_sent = get_effect_sent(text)
    sent_str = " ".join(sentences)

    data = lxr_ner_handle(sent_str)
    if not data:
        data = lxr_ner_handle(cad_sent)
    return str(dict(result=data))


def lxr_ner_handle(sent):
    entity = text_ner(sent, 'dict/lxr.txt')
    lxr_set = lxr_extract(entity)

    data = []
    for name in lxr_set:
        if name not in sxr:
            data.append(name)
    return data

