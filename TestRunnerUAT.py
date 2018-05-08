#!/usr/bin/python3

import configparser
import TestAll
import ENV

ENV.init('uat')
TestAll.processAll();
