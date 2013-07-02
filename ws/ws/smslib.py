#!/usr/bin/env python
from suds.client import Client

try:
    con = Client('url://')
except:
    pass

def send(mobile,message):
    username = None
    password = None
    serviceid = 'free'
    action = con.service.sendsms(username,password,mobile,message,serviceid)
    if action:
        return action
    else:
        return False