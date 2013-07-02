#!/usr/bin/env python

from pyws.server import SoapServer
from pyws.functions.register import register
from pymongo.connection import Connection
from ws.smslib import send

try:
    con = Connection('127.0.0.1',27017)
    db = con.smskeygen
except:
    pass #FIXME

server = SoapServer(
    service_name = 'smsws',
    tns = 'http://local.host',
    location = 'http://localhost:8000/api/',
)

@register()
def keygen(mobile,char=False):
    if not mobile.isdigit():
        return False
    
    key_range = map(chr,range(ord('1'),ord('9')))
    
    if char:
        for i in map(chr,xrange(ord('a'),ord('z'))):
            key_range.append(i)
            
    import random
    
    random.shuffle(key_range)
    
    keygen = random.sample(key_range,6)
    
    keygen = ''.join(keygen)
    
    send_id = send(mobile,keygen)
    
    if not send_id:
        return False
    
    db.users.insert({"mobile":mobile,"key":keygen,"status":"0","send":True,"send_id":send_id})
    
    return True

@register()
def check_sent(mobile):
    row = db.user.find_one({"mobile":mobile})
    if not row:
        return 3
    if row.get('send'):
        return True
    else:
        return False

@register()
def check_key(mobile,key):
    row = db.users.find({"mobile":mobile})
    if not row:
        return 3
    
    if row.get('key') != key:
        return False
    
    db.users.remove({"mobile":mobile},safe=True)
    
    return True