#!/usr/bin/env python

import unittest
from ws.smsws import *

class smsws_test(unittest.TestCase):
    def setUp(self):
        self.mobile = '09361752529'
    
    def test_keygen(self):
        result = keygen(self.mobile)
        self.assertTrue(result,'check mobile number')

        result = keygen(self.mobile,True)
        self.assertTrue(result,'check mobile number')