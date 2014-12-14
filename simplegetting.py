#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ownlib.getlocations import getlocations

import argparse
argh = argparse.ArgumentParser()
argh.add_argument('-a','--auth',action="store_true")
argh.add_argument('-t','--datatype',type=str,required=True)
argh.add_argument('-p','--person',action='append',type=str,required=True)
argh.add_argument('-u','--authtype',type=str)
argh.add_argument('-k','--authkey',type=str)
whentype = argh.add_mutually_exclusive_group(required=True)
whentype.add_argument('-s','--singlecheck',action="store_true")
whentype.add_argument('-e','--everyxseconds',type=float)
parmetry = vars(argh.parse_args())

ourinstance = getlocations(True if parmetry['auth'] else False,parmetry['authkey'] if parmetry['authkey'] else "There is no key",parmetry['authtype'] if parmetry['authtype'] else "nothing")

def checking(persons):
	for who in persons:
		for i in ourinstance.getsmbd(who,"dummy"): print i

if parmetry['singlecheck']:
	checking(parmetry['person'])
else:
	import time
	while True:
		checking(parmetry['person'])
		time.sleep(parmetry['everyxseconds'] if parmetry['everyxseconds'] else 1)