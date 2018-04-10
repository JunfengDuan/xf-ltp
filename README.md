# 信件 基本要素识别


## 分词工具：哈工大ltp算法包
## 启动服务：python3 recognize.py

### 请求地址
访问：http://host:8083/接口

###接口选择
受信人识别：sxr
来信人识别：lxr

调用身份证号识别接口 ： extract_id
调用手机号识别接口： extract_tel

地址识别：address
组织机构识别：org

分词：seg

传参格式{"text" : "..."}

返回数据格式：json字符串{"result":""}

## 词典使用
lexicon: 分词词典
lxr:来信人词典
sxr:受信人词典
rel:受信人名称关联词典

