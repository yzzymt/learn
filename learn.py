#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 23:13:16 2017

@author: jumpeat
"""

name = 'A'
age = 27

print 'My name is %s.'%(name)

print 'I\'m {} years old.'.format(age)

from datetime import datetime
now = datetime.now()

print now
print now.year
print now.month
print now.day

print '%s:%s:%s' % (now.hour, now.minute, now.second)