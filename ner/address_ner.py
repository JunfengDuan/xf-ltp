from ner.cn_ner import *
from dbconnect import connector

full_address = connector.get_full_address()


def address_ner(text):

    sent_str = text.replace('\n', '').replace(' ', '')

    entity = text_ner(sent_str)
    print('entity:', entity)
    address = address_extract(entity)
    list_full_address = [n[0] for n in full_address]
    print('recognised address:', address)
    print('list_full_address:', list_full_address)
    places = []
    if list_full_address and address:
        for s in address:
            match_place = get_top_score_address(s, list_full_address)
            places.extend(match_place)
    else:
        places = address
    print('places:', set(places))
    if places:
        places = rank_place(address, set(places))
    return str(dict(result=places))


def rank_place(address, places):
    rank = dict()
    for p in places:
        score = 0
        for d in address:
            score += match_score(d, p)
        rank[p] = score

    c = []
    for v in reversed(sorted(rank.values())):
        for k in rank.keys():
            if rank[k] == v and not c.__contains__(k):
                c.append(k)
    return c[0]


def get_top_score_address(source, target):
    max_score = 0.1
    max_score_address = ''
    multi_address = []
    for t in target:
        if len(t) == 0:
            continue

        score = match_score(source, t)
        if score > max_score:
            multi_address.clear()
            max_score, max_score_address = score, t
        elif score == max_score:
            multi_address.append(t)
    multi_address.append(max_score_address)
    print('max-score-address:', source, multi_address, max_score)
    return multi_address


def match_score(s, t):
    common_count = 0
    add_score = 0
    for i in s:
        if i in t:
            common_count += 1
    if common_count >= 2:
        if len(t) > len(s) and s in t:
            add_score += 0.5
        if t in s and len(t) > 6:
            add_score += 1
    else:
        add_score = 0
    if t in s:
        common_count = 0.5 * common_count
    score = common_count / len(t) + add_score
    return score
