#!/usr/bin/python3

import configparser
import TestLogin
import ENV




cf = configparser.ConfigParser()
cf.read('config/env-config.ini')


baseUrl = cf['sit']['baseUrl']
ENV.setBaseUrl(baseUrl);

deviceId = cf['sit']['deviceId']
ENV.setDeviceId(deviceId);

version = cf['sit']['version']
ENV.setVersion(version)

domain = cf['sit']['domain']
ENV.setDomain(domain)


print(baseUrl)
print(deviceId)
print(version)



TestLogin.process();
