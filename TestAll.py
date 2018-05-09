import TestLogin
import TestGetUserInfo
import TestGetIndex
import TestPassWordIsOverdue
import TestListTopic
import TestgetPushsCount
import TestbindUpushDeviceToken
import TestgetShowTabTaskCount
import TestgetIndexNoticeList
import Testsignin

def processAll():
    TestLogin.process();
    TestGetUserInfo.process();
    TestGetIndex.process();
    TestPassWordIsOverdue.process();
    TestListTopic.process();
    TestgetPushsCount.process();
    TestbindUpushDeviceToken.process();
    TestgetShowTabTaskCount.process();
    TestgetIndexNoticeList.process();
    Testsignin.process();