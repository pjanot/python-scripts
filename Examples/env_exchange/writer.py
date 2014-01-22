#!/bin/env python

import os
import shelve
import time

os.environ['TEST_ENV_VAR'] = 'here it is'
varlist = shelve.open('variables.txt')
varlist['environ'] = os.environ
time.sleep(20)
