#!/usr/bin/env python

from suds.client import Client

try:
    con = Client('http://127.0.0.1:8000/api/wsdl')
except Exception:
    print 'connection failed'
    sys.exit()
    
from flask import Flask,render_template

app = Flask(__main__)

@app.route('/')
def login():
    return render_template('login.html')
