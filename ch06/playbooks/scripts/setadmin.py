#!/usr/bin/env python
# A script to set the admin credentials
# Assumes two environment variables
#
# PROJECT_DIR: the project directory (e.g., ~/projname)
# ADMIN_PASSWORD: admin user's password

import os
import sys

# Add the project directory to system path
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

from django.core.wsgi import get_wsgi_applicatio
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = get_wsgi_application()


from mezzanine.utils.models import get_user_model
User = get_user_model()
u, _ = User.objects.get_or_create(username='admin')
u.is_staff = u.is_superuser = True
u.set_password(os.environ['ADMIN_PASSWORD'])
u.save()
