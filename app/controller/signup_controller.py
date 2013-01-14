import app_config

from app.controller.base_controller import BaseController
from oauth2client.appengine import OAuth2Decorator

# set up decorator
decorator = OAuth2Decorator(
  client_id=app_config.client_id,
  client_secret=app_config.client_secret,
  scope='https://www.googleapis.com/auth/userinfo'
)

class SignupController(BaseController):
  def get(self):
    pass