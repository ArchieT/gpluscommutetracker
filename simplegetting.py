#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ownlib.getlocations import getlocations

import argparse
argh = argparse.ArgumentParser()
argh.add_argument('-t','--datatype',type=str)
argh.add_argument('-p','--person',action='append',type=str)
argh.add_argument('-u','--authtype',type=str)
argh.add_argument('-a','--authkey',type=str)
whentype = argh.add_mutually_exclusive_group(required=True)
whentype.add_argument('-s','--singlecheck',action="store_true")
whentype.add_argument('-e','--everyxseconds',type=float)
parmetry = vars(argh.parse_args())

