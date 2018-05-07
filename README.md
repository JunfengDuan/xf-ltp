# 信件 基本要素识别


## 分词工具：哈工大ltp算法包
## 启动服务：python3 recognize.py

### 请求地址
访问：http://host:8083/接口

###接口选择
1.受信人识别：sxr

2.来信人识别：lxr

3.调用身份证号识别接口 ： extract_id

4.调用手机号识别接口： extract_tel

5.地址（归属地）识别：address

6.组织机构识别：org

7.分词：seg

8.统计人数：person_count

传参格式{"text" : "..."}

返回数据格式：json字符串{"result":""}

## 词典使用
lexicon: 分词词典

lxr:来信人词典

sxr:受信人词典

rel:受信人名称关联词典

## 数据库配置文件
jdbc.txt

