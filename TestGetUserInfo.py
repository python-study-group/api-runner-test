import urllib.request
import ENV
import json

def process():
    print("TestGetUserInfo.py process~~~")
    print('baseUrl is : ' + ENV.getBaseUrl())
    #send_data = "username=jinron_EL&password=Aa123456";
    #send_data_urlencode = urllib.urlencode(send_data);
    #send_data_bytes = bytes(send_data, encoding='utf8')

    requrl = ENV.getBaseUrl() + "/api/getUserInfo";
    headerdata = {"version": ENV.getVersion() , "Content-Type": "application/x-www-form-urlencoded", "deviceId": ENV.getDeviceId(),"apikey": ENV.getToken()}

    req = urllib.request.Request(url=requrl,  headers=headerdata)
    print(req)

    res_data = urllib.request.urlopen(req)
    response_bytes = res_data.read()
    #print(response_bytes)

    str_from_utf_8 = response_bytes.decode(encoding="utf-8")
    print(str_from_utf_8)

    response_json = json.loads(str_from_utf_8)
    if  0 == response_json['error_code'] :
        print('get user info process success');
    else:
        print('error_code is not 0');



