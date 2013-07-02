#!/usr/bin/env python

import unittest
from ws.smsws import *

class smsws_test(unittest.TestCase):
    def setUp(self):
        self.mobile = '09361752529'
        self.key = '123456'
        
    def test_keygen(self):
        result = keygen(self.mobile)
        self.assertTrue(result,'check mobile number')

        result = keygen(self.mobile,True)
        self.assertTrue(result,'check mobile number')
        
    def test_check_sent(self):
        check = check_sent(self.mobile)
        
        self.assertEqual(check,'3','user record not found')
        
        self.assertFalse(check,'your send field is not true')
        
        self.assertTrue(check)
        
    def test_check_key(self):
        check = check_key(self.mobile,self.key)
        
        self.assertEqual(check,'3','user record not found')
        
        self.assertFalse(check,'invalid key')
        
        self.assertTrue(check)
    