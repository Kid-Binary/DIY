# act_project/act/act/wsgi.py
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "act.settings.prod")

application = get_wsgi_application()
