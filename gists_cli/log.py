#!/usr/bin/env python

import sys
from datetime import datetime

#-------------------------------------------

debugEnabled = False

def setDebug (debug):
  global debugEnabled
  debugEnabled = debug

def comment (obj):
  print('>> ' + str(obj))

def debug (obj):
  if debugEnabled:
    print('[' + str(datetime.now()) + ']: ' + str(obj))

def error (obj):
  print('ERROR: ' + str(obj))

def printDict (obj):
  for k,v in list(obj.items()):
    print(k,v)
