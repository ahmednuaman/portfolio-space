import jinja2

from app.helper import file_helper

def load(name, data={}):
  # set the file
  file = '%s_view.html' % name

  # set the folder
  folder = 'app/view/'

  # and the path
  path = folder + file

  # check for the file in memcache
  view = memcache.get(path)

  if not view:
    # check the file exists
    if not file_helper.check(path):
      # uh oh
      raise IOError('File %s not found' % path)

    # set up env for the renderer
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(folder))

    # prepare the template
    template = env.get_template(file)

    # render the view
    view = template.render(data)

    # save it to memcache
    memcache.set(path, view)

  # return it
  return view