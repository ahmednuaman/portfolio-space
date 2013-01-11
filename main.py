import webapp2
import webapp2_config

from app.controller import admin_controller, manage_controller, page_controller, signup_controller

config = webapp2_config

app = webapp2.WSGIApplication([
  (signup_controller.decorator.callback_path, signup_controller.decorator.callback_handler()),
  ('/admin/', admin_controller.AdminController),
  ('/signup/', signup_controller.SignupController),
  ('/manage/', manage_controller.ManageController),
  (r'/([^\/]+)?', page_controller.PageController)
], config=config)