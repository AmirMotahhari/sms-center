#!/usr/bin/env python

from suds.client import Client

try:
    soap = Client('http://127.0.0.1:8000/api/wsdl')
except Exception:
    print 'connection failed\nCheck your web service status!'
    sys.exit()
    
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def send():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        sv = soap.service.check_sent(mobile)
        
        if sv == '3':
            action = soap.service.keygen(mobile)
            msg = 'key generated and sent to your phone'
        else:
            action = soap.service.keygen(mobile)
            msg = 'key resent to your phone'
        return msg
    return render_template('send.html')

@app.route('/verify',methods=['GET','POST'])
def verify():
    if request.method == "POST":
        mobile = request.form.get('mobile')
        key = request.form.get('key')
        if not mobile or not key or not mobile.isdigit():
            return 'Enter correct data!'
        
        check = soap.service.check_key(mobile,key)
        
        if check == '3':
            return 'You didnt register your phone number at / addr'
        elif check == 'False':
            return 'your key is not correct! try again.'
        
        return 'Yes! your key is correct!'
    return render_template('verify.html')


if __name__ == "__main__":
    app.run(debug=True)