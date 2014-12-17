# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
import cgi
from google.appengine.api import users
import webapp2

MAIN_PAGE_HTML = file('main-html.html').read()

class MainPage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/html'
			self.response.write(MAIN_PAGE_HTML + user.nickname())
		else:
			self.redirect(users.create_login_url(self.request.uri))
class Adding(webapp2.RequestHandler):
	def adding(self):
		self.response.write('<html><body>You entered:<pre>')
		self.response.write(cgi.escape(self.request.get('profileID')))
		self.response.write(cgi.escape(self.request.get('forever')))
		self.response.write(" until ")
		self.response.write(cgi.escape(self.request.get('until')))
		self.response.write(" every ")
		self.response.write(cgi.escape(self.request.get('every')))
		self.response.write(" minutes")
		self.response.write('</pre></body></html>')

application = webapp2.WSGIApplication([
	('/', MainPage),
	('/adding', Adding)
], debug=True)