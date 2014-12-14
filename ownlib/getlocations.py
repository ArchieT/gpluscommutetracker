# -*- coding: utf-8 -*-
class getlocations:
	def __init__(self,auth,authkey="There is no key",authkeytype="nothing"):
		if auth:
			self.wherefrom = getfromauth(authkey,authkeytype)
		else:
			self.wherefrom = getfrompub()

	def getsmbd(self,who,how):
		whereishe = self.wherefrom.getsomebody(who,how)
		return whereishe

class getfromauth:
	def __init__(self,authkey,authkeytype):
		if authkeytype == "nothing" and authkey == "There is no key":
			print "There is no key and it's type's nothing, thus exiting."
			quit()
		if authkeytype == "dummy":
			print "This is a dummy authkeytype, fake data will appear."
		if authkeytype == "plainpasswd":
			password = authkey
	def getsomebody(self,who,how):
		if how == "dummy":
			print "Fake data is served through auth"
			fakedictlist = [
				{"firstperson": {"loc": [53.945877,18.345667],"timewas": 1418563216},"secondperson": {"loc": [58.435666,14.416776],"timewas": 1418562100}},
				{"firstperson": {"loc": [53.945877,18.345667],"timewas": 1418563416},"secondperson": {"loc": [58.445666,14.426776],"timewas": 1418562200}},
				{"firstperson": {"loc": [53.922877,18.335667],"timewas": 1418563816},"secondperson": {"loc": [58.455666,14.436776],"timewas": 1418562300}},
				{"firstperson": {"loc": [53.933877,18.325667],"timewas": 1418564016},"secondperson": {"loc": [58.465666,14.446776],"timewas": 1418562400}},
				{"firstperson": {"loc": [53.956877,18.315667],"timewas": 1418564216},"secondperson": {"loc": [58.475666,14.456776],"timewas": 1418562500}},
				{"firstperson": {"loc": [53.995877,18.305667],"timewas": 1418564416},"secondperson": {"loc": [58.485666,14.466776],"timewas": 1418562600}},
				{"firstperson": {"loc": [53.915877,18.395667],"timewas": 1418564616},"secondperson": {"loc": [58.495666,14.476776],"timewas": 1418562700}},
			]
			from random import randint
			fakenum = randint(0,len(fakedictlist)-1)
			fakedict = fakedictlist[fakenum]
			import time
			return {"got": fakedict[who],"gettime": time.time()}
class getfrompub:
	def __init__(self):
		pass # prepare the connection
	def getsomebody(self,who,how):
		if how == "dummy":
			print "Fake data is served through pub"
			fakedictlist = [
				{"firstperson": {"loc": [53.945877,18.345667],"timewas": 1418563216},"secondperson": {"loc": [58.435666,14.416776],"timewas": 1418562100}},
				{"firstperson": {"loc": [53.945877,18.345667],"timewas": 1418563416},"secondperson": {"loc": [58.445666,14.426776],"timewas": 1418562200}},
				{"firstperson": {"loc": [53.922877,18.335667],"timewas": 1418563816},"secondperson": {"loc": [58.455666,14.436776],"timewas": 1418562300}},
				{"firstperson": {"loc": [53.933877,18.325667],"timewas": 1418564016},"secondperson": {"loc": [58.465666,14.446776],"timewas": 1418562400}},
				{"firstperson": {"loc": [53.956877,18.315667],"timewas": 1418564216},"secondperson": {"loc": [58.475666,14.456776],"timewas": 1418562500}},
				{"firstperson": {"loc": [53.995877,18.305667],"timewas": 1418564416},"secondperson": {"loc": [58.485666,14.466776],"timewas": 1418562600}},
				{"firstperson": {"loc": [53.915877,18.395667],"timewas": 1418564616},"secondperson": {"loc": [58.495666,14.476776],"timewas": 1418562700}},
			]
			from random import randint
			fakenum = randint(0,len(fakedictlist)-1)
			fakedict = fakedictlist[fakenum]
			import time
			return {"got": fakedict[who],"gettime": time.time()}