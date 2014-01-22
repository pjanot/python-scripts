#!/bin/env python

import os
import shelve

varlist = shelve.open('variables.txt')
print varlist['environ']['TEST_ENV_VAR']

