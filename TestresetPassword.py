import urllib.request
import ENV
import json
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s :  %(message)s')
logger = logging.getLogger(__name__)

def process():
    logger.info("TestgetresetPassword.py process~~~")
    logger.info('baseUrl is' + ENV.getBaseUrl())
    send_data = "username=jinron_el";
    send_data_bytes = bytes(send_data,encoding='utf8')

    requrl = ENV.getBaseUrl() + "/api/resetPassword";
    headerdata = {"version": ENV.getVersion() , "Content-Type": "application/x-www-form-urlencoded","deviceId":ENV.deviceId,"apiKey":ENV.getToken()}

    req = urllib.request.Request(url=requrl,data=send_data_bytes,headers=headerdata)
    logger.info(req)

    res_data = urllib.request.urlopen(req)
    response_bytes = res_data.read()

    str_from_utf_8 = response_bytes.decode(encoding="utf-8")
    logger.info(str_from_utf_8)

    response_json = json.loads(str_from_utf_8)
    if 0 == response_json['error_code']:
        logger.error("error_code is not 0");#断言Error Code
    else :
        1 == response_json['error_code'];
        logger.error('error_code is not 0');
