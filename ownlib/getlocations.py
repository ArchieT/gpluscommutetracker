# -*- coding: utf-8 -*-
class getlocations:
	def __init__(self,auth,authkey="There is no key",authkeytype="nothing"):
		if auth:
			getfromauth(authkey,authkeytype)
class getfromauth:
	def __init__(self,authkey,authkeytype):
		if authkeytype == "nothing" and authkey == "There is no key":
			print "There is no key and it's type's nothing, thus exiting."
			quit()
		if authkeytype == "dummy":
			print "This is a dummy authkeytype, fake data will appear."
class getfrompub:
	def __init__(self):
