#!/usr/bin/env python
from suds.client import Client
from settings import WEB_SERVICE


try:
    con = Client('url://')
except:
    pass

def send(mobile,message):
    string_args = "%s.%s('%s')" % ('con.service',WEB_SERVICE['service'],"','".join(WEB_SERVICE['argv']).format(message=message,mobile=mobile))
    action = eval(string_args)
    if action:
        return action
    else:
        return False
