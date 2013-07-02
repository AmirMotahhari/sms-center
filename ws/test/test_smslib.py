#!/usr/bin/env python

import unittest

class smslib_test(unittest.TestCase):
    def setup(self):
        self.mobile = '09361752529'
        self.key = '4423fd'
    
    def test_send(self):
        check = send(self.mobile,self.key)
        self.assertRegexpMatches(check,'[a-z0-9]')
