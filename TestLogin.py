import urllib.request
import ENV


def process():
    print("TestLogin.py process~~~")
    print('baseUrl is : ' + ENV.getBaseUrl())
    send_data = "username=jinron_EL&password=Aa123456";
    #send_data_urlencode = urllib.urlencode(send_data);
    send_data_bytes = bytes(send_data, encoding=
    'utf8')

    requrl = ENV.getBaseUrl() + "/api/login";
    headerdata = {"version": ENV.getVersion() , "Content-Type": "application/x-www-form-urlencoded", "deviceId": ENV.getDeviceId()}

    req = urllib.request.Request(url=requrl, data=send_data_bytes, headers=headerdata)
    print(req)

    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    print(res)


