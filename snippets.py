from google.appengine.ext import ndb

class MyUser(ndb.Model):
    USERNAME = ndb.StringProperty()
    TWEET = ndb.StringProperty(repeated==True)
    FOLLOWERS = ndb.StringProperty(repeated==True)
