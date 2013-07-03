#!/usr/bin/env python
from suds.client import Client
from settings import WEB_SERVICE

if len(WEB_SERVICE['connect']['argv']):
    string_args = "('%s','%s')" % (WEB_SERVICE['connect']['url'],"','".join(WEB_SERVICE['connect']['argv']))
else:
    string_args = "('%s')" % WEB_SERVICE['connect']['url']
print string_args

try:
    con = Client(string_args)
except:
    pass


def send(mobile,message):
    for i in WEB_SERVICE:
        if "step" in i:
            string_args = "%s.%s('%s')" % ('con.service',WEB_SERVICE[i]['service'],"','".join(WEB_SERVICE[i]['argv']).format(message=message,mobile=mobile))
            action = eval(string_args)
            if not action:
                return False
    if action:
        return action
    else:
        return False