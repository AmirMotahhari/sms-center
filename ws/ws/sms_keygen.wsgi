import os
import sys
import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'ws.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

path = settings.PROJECT_PATH;
if path not in sys.path:
    sys.path.append(path)