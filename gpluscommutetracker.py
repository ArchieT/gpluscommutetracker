# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
import cgi
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2

#MAIN_PAGE_HTML = file('main-html.html').read()
MAIN_PAGE_FOOTER = """\
	<form action="/adding" method="post">
		<div>Profile ID: <input name="profileid" type="text"></div>
		<div> track <input type="checkbox" name="forever" value="forever"> forever / until <input name="until" type="datetime"></div>
		<div> every <input type="number" name="every"> minutes</div>
		<div><input type="submit" value="Start tracking"></div>
	</form>
</body>
</html>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/html'
			#self.response.write(MAIN_PAGE_HTML + user.nickname())
			self.response.write('<html><body bgcolor="#FFFFCC">')
			databaza_name = self.request.get('databaza_name', 'dbinstancje_ongoing')
			instances_query = Instance.query(ancestor=ndb.Key('databaza','dbinstancje_ongoing')).order(-Instance.creationdate)
			instances = instances_query.fetch(1000)

			for instance in instances:
				self.response.write("owner: %s profileID: %s until: %s every: %s forever: %s creationdate: %s" % (
					instance.owner.nickname(),
					instance.profileID(),
					instance.until(),
					instance.every(),
					instance.forever(),
					instance.creationdate()
				))

			adding_query_params = urllib.urlencode({'databaza_name': databaza_name})
			self.response.write(MAIN_PAGE_FOOTER % adding_query_params)
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

class Instance(ndb.Model):
	owner = ndb.UserProperty()
	profileID = ndb.StringProperty(indexed=False)
	until = ndb.DateTimeProperty(auto_now_add=False)
	every = ndb.StringProperty(indexed=False)
	forever = ndb.StringProperty(indexed=False)
	creationdate = ndb.DateTimeProperty(auto_now_add=True)

class Databaza(webapp2.RequestHandler):
	def post(self):
		databaza_name = self.request.get('databaza_name','dbinstancje_ongoing')
		instance = Instance(parent=ndb.Key('databaza',databaza_name))
		instance.owner = users.get_current_user()
		instance.profileID = self.request.get('profileID')
		instance.until = self.request.get('until')
		instance.every = self.request.get('every')
		instance.forever = self.request.get('forever')
		instance.put()
		query_params = {'databaza_name': databaza_name}
		self.redirect('/?'+urllib.urlencode(query_params))

application = webapp2.WSGIApplication([
	('/', MainPage),
	('/adding', Adding)
], debug=True)