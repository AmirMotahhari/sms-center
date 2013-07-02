#!/usr/bin/env python

from pyws.server import SoapServer
from pyws.functions.register import register
from pymongo.connection import Connection

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
    
    db.users.insert({"mobile":mobile,"key":keygen,"status":"0"})
    
    return ''.join(keygen)

@register()
def checksent(mobile):
    pass
