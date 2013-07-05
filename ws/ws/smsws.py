#!/usr/bin/env python

from pyws.server import SoapServer
from pyws.functions.register import register
from pymongo.connection import Connection
from ws.smslib import send
import sys
from settings import *

try:
    con = Connection(DATABASE_HOST,DATABASE_PORT)
    db = con[DATABASE_NAME]
    logging.info('db:connect: %s:%s' % (DATABASE_HOST,DATABASE_PORT))
except:
    logging.error('db:connect error: %s:%s' % (DATABASE_HOST,DATABASE_PORT))
    sys.exit()

server = SoapServer(
    service_name = SOAP_NAME,
    tns = SOAP_TNS,
    location = SOAP_LOCATION,
)

@register()
def keygen(username=None,password=None,mobile,char=False):
    if not username or not password:
        return 403
    #implementing 401
    if not mobile.isdigit():
        logging.warning("keygen:invalid mobile: %s" % mobile)
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
    
    row = db.users.find_one({"mobile":mobile})

    if not row:
        db.users.insert({"mobile":mobile,"key":keygen,"status":"0","send":True,"send_id":send_id},safe=True)
        logging.info("keygen,db:insert data: %s" % ('-'.join({"mobile":mobile,"key":keygen,"status":"0","send":True,"send_id":send_id})))
    else:
        row['key'] = keygen
        db.users.update({"mobile":mobile},row,safe=True)
        logging.info("keygen,db:update data: %s" % ('-'.join({"mobile":mobile,"key":keygen})))
    return True

@register()
def check_sent(username=None,password=None,mobile):
    if not username or not password:
        return 403
    #implementing 401
    row = db.users.find_one({"mobile":mobile})
    if not row:
        logging.warning("check_sent:not found mobile: %s" % mobile)
        return 3
    if row.get('send'):
        logging.info("check_sent:success mobile: %s" % mobile)
        return True
    else:
        logging.info("check_sent:failed mobile: %s" % mobile)
        return False

@register()
def check_key(username=None,password=None,mobile,key):
    if not username or not password:
        return 403
    #implementing 401
    row = db.users.find_one({"mobile":mobile})
    if not row:
        logging.warning("check_key:not found mobile: %s" % mobile)
        return 3
    
    if row.get('key') != key:
        logging.warning("check_key:invalid key: %s mobile: %s" % (key,mobile))
        return False
    
    db.users.remove({"mobile":mobile},safe=True)
    logging.info("check_key,db:[success key]remove row mobile: %s" % mobile)   
    return True
