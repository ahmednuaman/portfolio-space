import webapp2
import webapp2_config

from app.controller import admin_controller, page_controller

config = webapp2_config

app = webapp2.WSGIApplication([
  (admin_controller.decorator.callback_path, admin_controller.decorator.callback_handler()),
  ('/admin/', admin_controller.AdminController),
  (r'/([^\/]+)?', page_controller.PageController)
], config=config)