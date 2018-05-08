import configparser

# 告诉编译器这是全局变量a
global baseUrl

def setBaseUrl(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global baseUrl
    baseUrl = value

def getBaseUrl():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global baseUrl
    return baseUrl


# 告诉编译器这是全局变量a
global deviceId

def setDeviceId(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global deviceId
    deviceId = value

def getDeviceId():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global deviceId
    return deviceId


# 告诉编译器这是全局变量a
global version

def setVersion(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global version
    version = value

def getVersion():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global version
    return version


# 告诉编译器这是全局变量a
global domain

def setDomain(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global domain
    domain = value

def getDomain():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global domain
    return domain


# 告诉编译器这是全局变量a
global token

def setToken(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global token
    token = value

def getToken():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global token
    return token



def init(environment):
    cf = configparser.ConfigParser()
    cf.read('config/env-config.ini')

    baseUrl = cf[environment]['baseUrl']
    setBaseUrl(baseUrl);

    deviceId = cf[environment]['deviceId']
    setDeviceId(deviceId);

    version = cf[environment]['version']
    setVersion(version)

    domain = cf[environment]['domain']
    setDomain(domain)

    print(baseUrl)
    print(deviceId)
    print(version)