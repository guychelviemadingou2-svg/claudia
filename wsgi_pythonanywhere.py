# Configuration pour PythonAnywhere
import os
import sys

# Chemin vers votre projet
path = '/home/VOTRE_USERNAME/claudia'
if path not in sys.path:
    sys.path.insert(0, path)

# Variables d'environnement
os.environ['DJANGO_SETTINGS_MODULE'] = 'monapp.settings'

# Application WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()