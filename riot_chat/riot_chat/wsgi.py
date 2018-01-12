"""
WSGI config for riot_chat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "riot_chat.settings")

import riot_chat.startup as startup
acc_token = startup.run()

application = get_wsgi_application()
