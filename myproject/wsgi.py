import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
virtenv =os.path.join(os.environ['HOME'],'webapps','djangoer','djenv','bin','activate_this.py')
try:
    execfile(virtenv, dict(__file__=virtenv))
except IOError:
    pass

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
