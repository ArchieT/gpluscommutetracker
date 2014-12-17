# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from google.appengine.api import users
import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/html'
			self.response.write('Zażółć gęślą jaźń, ' + user.nickname())
		else:
			self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)