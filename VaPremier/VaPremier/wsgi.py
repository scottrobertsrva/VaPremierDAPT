"""
WSGI config for VaPremier project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

import sys
sys.path.append("/var/www/VaPremier")
os.environ.setdefault("PYTHON_EGG_CACHE","/var/www/VaPremier/egg_cache")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VaPremier.settings")
application = get_wsgi_application()
