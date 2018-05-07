# coding:utf-8
import pymysql

# conn = pymysql.connect(host="192.168.3.171", port=3306, user="root", password="123456", db="xfj_znfz", charset='utf8')
conn = pymysql.connect(host="localhost", port=3306, user="jfd", password="jfd", db="xfj_znfz", charset='utf8')


def get_full_address():

    with conn.cursor() as cursor:
        sql = "SELECT full_name FROM xzqh"
        cursor.execute(sql)
        records = cursor.fetchall()

    return records
