from google.appengine.ext import db

class Post(db.Model):
	#author = db.StringProperty()
	content = db.StringProperty(multiline=True)
	postdate = db.DateTimeProperty(auto_now_add=True)


