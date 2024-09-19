"""
ASGI configuration for the hospital management system project.

This module exposes the ASGI callable as a variable named ``application``.

For more details, refer to:
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_management.settings')

application = get_asgi_application()
