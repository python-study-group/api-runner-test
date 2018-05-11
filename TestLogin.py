import urllib.request
import ENV
import json
import configparser

import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s :  %(message)s')
logger = logging.getLogger(__name__)

def process():
    logger.info("TestLogin.py process~~~")
    logger.info('baseUrl is : ' + ENV.getBaseUrl())

    cf = configparser.ConfigParser()
    cf.read('config/env-config.ini')
    username = cf[ENV.getEnvironment()]['username']
    password = cf[ENV.getEnvironment()]['password']
    send_data = "username="+ username + "&password="+password;
    #send_data_urlencode = urllib.urlencode(send_data);
    send_data_bytes = bytes(send_data, encoding='utf8')

    requrl = ENV.getBaseUrl() + "/api/login";
    headerdata = {"version": ENV.getVersion() , "Content-Type": "application/x-www-form-urlencoded", "deviceId": ENV.getDeviceId()}

    req = urllib.request.Request(url=requrl, data=send_data_bytes, headers=headerdata)
    logger.info(req)

    res_data = urllib.request.urlopen(req)
    response_bytes = res_data.read()
    #print(response_bytes)

    str_from_utf_8 = response_bytes.decode(encoding="utf-8")
    logger.info(str_from_utf_8)

    response_json = json.loads(str_from_utf_8)
    assert 0 == response_json['error_code'], logger.error("error_code is not 0");

    token = response_json['data']['token']
    logger.info('token is : ' + token)
    ENV.setToken(token)




