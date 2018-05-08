import urllib.request
import ENV
import json

def process():
    print("TestLogin.py process~~~")
    print('baseUrl is : ' + ENV.getBaseUrl())
    send_data = "username=jinron_EL&password=Aa123456";
    #send_data_urlencode = urllib.urlencode(send_data);
    send_data_bytes = bytes(send_data, encoding='utf8')

    requrl = ENV.getBaseUrl() + "/api/login";
    headerdata = {"version": ENV.getVersion() , "Content-Type": "application/x-www-form-urlencoded", "deviceId": ENV.getDeviceId()}

    req = urllib.request.Request(url=requrl, data=send_data_bytes, headers=headerdata)
    print(req)

    res_data = urllib.request.urlopen(req)
    response_bytes = res_data.read()
    #print(response_bytes)

    str_from_utf_8 = response_bytes.decode(encoding="utf-8")
    print(str_from_utf_8)

    response_json = json.loads(str_from_utf_8)
    if  0 == response_json['error_code'] :
        token = response_json['data']['token']
        print('token is : ' + token)
        ENV.setToken(token)
    else:
        print('error_code is not 0');



