#-*- coding: utf-8 -*-
"""
    Guardar as informações de usuário e senha no banco 
"""
from google.appengine.ext import db

class Credentials(db.Model):
  email = db.StringProperty()
  password = db.StringProperty()
  # key_name='psn'
  # c.put()
  
def retrieve_psn_credentials() :
  psn_credentials_key = db.Key.from_path('Credentials', 'psn')
  return db.get(psn_credentials_key)
