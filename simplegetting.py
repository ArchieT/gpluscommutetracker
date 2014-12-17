#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ownlib.getlocations import getlocations
from oauth2client import tools
import argparse
argh = argparse.ArgumentParser(parents=[tools.run_parser])
argh.add_argument('-a','--auth',action="store_true")
argh.add_argument('-t','--datatype',type=str,required=True)
argh.add_argument('-p','--person',action='append',type=str,required=True)
argh.add_argument('-u','--authtype',type=str)
argh.add_argument('-k','--authkey',type=str)
whentype = argh.add_mutually_exclusive_group(required=True)
whentype.add_argument('-s','--singlecheck',action="store_true")
whentype.add_argument('-e','--everyxseconds',type=float)
parmetery = argh.parse_args()
parmetry = vars(parmetery)

if parmetry['auth'] and False:
	from oauth2client.file import Storage
	credentials = 12345
	storage = Storage('credentials')



ourinstance = getlocations(True if parmetry['auth'] else False,parmetry['authkey'] if parmetry['authkey'] else "There is no key",parmetry['authtype'] if parmetry['authtype'] else "nothing")

def checking(persons):
	whatweregettin = {}
	for whocreate in persons: whatweregettin[whocreate] = []
	for who in persons:
		thisisit = ourinstance.getsmbd(who,"dummy")
		for i in thisisit:
			print i
			print thisisit[i]


if parmetry['singlecheck']:
	checking(parmetry['person'])
else:
	import time
	while True:
		checking(parmetry['person'])
		time.sleep(parmetry['everyxseconds'] if parmetry['everyxseconds'] else 1)