"""
WSGI config for clean project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/opt/bitnami/apps/django/django_projects/clean')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/clean/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clean.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()