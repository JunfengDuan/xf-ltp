# coding:utf-8
import pymysql
import os
# conn = pymysql.connect(host="192.168.3.171", port=3306, user="root", password="123456", db="xfj_znfz", charset='utf8')
# conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
conn = None
jdbc_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'jdbc.txt')


def get_full_address():
    global conn
    if conn is None:
        conn = read_jdbc()

    with conn.cursor() as cursor:
        sql = "SELECT full_name FROM xzqh"
        cursor.execute(sql)
        records = cursor.fetchall()

    return records


def read_jdbc():
    with open(jdbc_file_path, 'r', encoding='utf-8') as f:
        prop_dict = dict()
        for p in f.readlines():
            kv = p.split('=')
            value = kv[1].replace('\n', '').replace(' ', '')
            prop_dict[kv[0]] = value
    host, port, user, password, db = prop_dict['host'], int(prop_dict['port']), prop_dict['user'], \
                                     prop_dict['password'], prop_dict['db']
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
    return conn


# if __name__ == '__main__':
    # print(read_jdbc())