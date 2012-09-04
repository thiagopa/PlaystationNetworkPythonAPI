from google.appengine.ext import db

class Credentials(db.Model):
  email = db.StringProperty()
  password = db.StringProperty()
  # key_name='psn'
  
def retrieve_psn_credentials() :
  psn_credentials_key = db.Key.from_path('Credentials', 'psn')
  return db.get(psn_credentials_key)
