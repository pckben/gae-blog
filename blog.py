import webapp2
import jinja2
import os

from google.appengine.api import users

from models import *

jinja_environment = jinja2.Environment(
		loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
	def get(self):
		values = {
		}
		template = jinja_environment.get_template('index.jinja.html')
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write(template.render(values))

class Post(webapp2.RequestHandler):
	def get(self):
		blogid = self.request.get('id')
		self.response.write(blogid)
	
	def create(self):
		post = models.Post()

	def save(self):
		pass

app = webapp2.WSGIApplication(
		[
			('/', MainPage),
			
		], 
		debug=True)
