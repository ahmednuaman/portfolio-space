import webapp2
import webapp2_config

from app.controller import admin_controller, manage_controller, profile_controller, signup_controller

config = webapp2_config

app = webapp2.WSGIApplication([
  (signup_controller.decorator.callback_path, signup_controller.decorator.callback_handler()),
  ('/admin/', admin_controller.AdminController),
  ('/manage/', manage_controller.ManageController),
  (r'/([^\/]+)', profile_controller.ProfileController),
  ('/', signup_controller.SignupController)
], config=config)