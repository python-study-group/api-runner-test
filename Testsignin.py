import urllib.request
import ENV
import json
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s :  %(message)s')
logger = logging.getLogger(__name__)

def process():
    logger.info("Testsignin.py process~~~")#记录日志
    logger.info('baseUrl is :' + ENV.getBaseUrl())#记录日志

    requrl = ENV.getBaseUrl() + "/api/signin";#拼接首页的URL
    headerdata = {"version": ENV.getVersion() , "Content-Type": "application/x-www-form-urlencoded","deviceId":ENV.deviceId,"apiKey":ENV.getToken()}
    #组装Header
    req = urllib.request.Request(url=requrl,headers=headerdata)#定义一个请求
    logger.info(req)#记录日志请求

    res_data = urllib.request.urlopen(req)#开始发送请求
    response_bytes = res_data.read()#读取返回的内容
    #print(response_bytes)

    str_from_utf_8 = response_bytes.decode(encoding="utf-8")#将内容转换为字符串
    logger.info(str_from_utf_8)#日志输出字符串

    response_json = json.loads(str_from_utf_8)#将字符串转换为json
    if 0 == response_json['error_code']:
        logger.error("error_code is not 0");#断言Error Code
    else :
        1 == response_json['error_code'];
        logger.error('error_code is not 0');