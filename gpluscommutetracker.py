# -*- coding: utf-8 -*-
__author__ = 'mf'
import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('Zażółć gęślą jaźń')

application = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)