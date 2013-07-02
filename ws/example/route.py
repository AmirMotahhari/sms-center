#!/usr/bin/env python

from suds.client import Client

try:
    con = Client('http://127.0.0.1:8000/api/wsdl')
except Exception:
    print 'connection failed'
    sys.exit()
    
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def send():
    return render_template('send.html')

@app.route('/verify')
def verify():
    return render_template('verify.html')


if __name__ == "__main__":
    app.run(debug=True)