import webapp2

from webapp2_extras import sessions

class BaseController(webapp2.RequestHandler):
  def dispatch(self):
    # get a session store for this request.
    self._session_store = sessions.get_store(request=self.request)

    try:
      # dispatch the request.
      webapp2.RequestHandler.dispatch(self)

    finally:
      # save all sessions.
      self._session_store.save_sessions(self.response)

  @webapp2.cached_property
  def session(self):
    # returns a session using the default cookie key.
    return self._session_store.get_session()