# coding:utf-8
from flask import Flask, request
from flask_cors import CORS
from ner.sxr_ner import sxr_ner
from ner.lxr_ner import lxr_ner
from ner.org_ner import org_ner
from ner.address_ner import address_ner
from ner.person_ner import name_count
from rule.rule_number import *
import ner.cn_ner as ner


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/org', methods=['GET', 'POST'])
def org():

    text = request.get_json().get('text')
    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    response = org_ner(text)
    print('\nresponse:', response)

    return response


@app.route('/address', methods=['GET', 'POST'])
def address():

    text = request.get_json().get('text')
    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    response = address_ner(text)
    print('\nresponse:', response)

    return response


@app.route('/sxr', methods=['GET', 'POST'])
def sxr():

    text = request.get_json().get('text')
    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    response, _ = sxr_ner(text)
    print('\nresponse:', response)

    return response


@app.route('/lxr', methods=['GET', 'POST'])
def lxr():
    text = request.get_json().get('text')
    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    response = lxr_ner(text)
    print('\nresponse:', response)

    return response


@app.route('/extract_id', methods=['GET', 'POST'])
def extract_id():

    text = request.get_json().get('text')
    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    id_card = id_recognition(text)
    print('id_card:', id_card)

    return id_card


@app.route('/extract_tel', methods=['GET', 'POST'])
def extract_tel():

    text = request.get_json().get('text')

    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    phone_num = phone_number_recognition(text)
    print('phone_num:', phone_num)

    return phone_num


@app.route('/seg', methods=['GET', 'POST'])
def seg():

    text = request.get_json().get('text')

    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    segment = ner.only_seg(text, lexicon_path='dict/lexicon.txt')
    print('segment:', segment)

    return segment


@app.route('/person_count', methods=['GET', 'POST'])
def person_count():

    text = request.get_json().get('text')

    print('text:', text)

    if text is None or len(text) == 0:
        return ""

    count = name_count(text, lexicon_path='dict/lexicon.txt')
    print('name_count:', count)

    return count


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8083, debug=True)

