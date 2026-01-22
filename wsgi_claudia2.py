# WSGI config for claudia2.pythonanywhere.com
import os
import sys

# Ajouter le chemin de votre projet
path = '/home/claudia2/claudia'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'monapp.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()