import cgi, wsgiref.handlers, logging#,random, yaml
#from django.utils import simplejson as json
#from google.appengine.api import users, mail
#from datetime import datetime
from google.appengine.ext import webapp
from mvc import  models, util, controllers

application = webapp.WSGIApplication([
    ('/',controllers.index),
    ('.*',util.Error404)
  ],
  debug=True
)

def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__': main()
