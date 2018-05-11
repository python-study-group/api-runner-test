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
import TestgetPushList
import TestreadAllPushs
import TestgetPushDetail
import TestdeletePushs
import TestresetPassword
import TestgetHotwords
import TestlistTopClassify
import Testsearch

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
    TestgetPushList.process();
    TestreadAllPushs.process();
    TestgetPushDetail.process();
    TestdeletePushs.process();
    TestresetPassword.process();
    TestgetHotwords.process();
    TestlistTopClassify.process();
    Testsearch.process();