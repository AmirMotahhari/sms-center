#!/usr/bin/env python
from suds.client import Client
from settings import WEB_SERVICE,logging
import sys

if len(WEB_SERVICE['connect']['argv']):
    string_args = "('%s','%s')" % (WEB_SERVICE['connect']['url'],"','".join(WEB_SERVICE['connect']['argv']))
else:
    string_args = "('%s')" % WEB_SERVICE['connect']['url']

try:
    con = Client(string_args)
    logging.info('soap:connect: %s' % string_args)
except:
    logging.error('soap:connect error: %s' % string_args)
    sys.exit()


def send(mobile,message):
    for i in WEB_SERVICE:
        if "step" in i:
            string_args = "%s.%s('%s')" % ('con.service',WEB_SERVICE[i]['service'],"','".join(WEB_SERVICE[i]['argv']).format(message=message,mobile=mobile))
            action = eval(string_args)
            logging.info('service:connect: %s' % string_args)
            if not action:
                return False
    if action:
        return action
    else:
        return False