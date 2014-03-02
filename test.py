#!/usr/bin/env python
from django.core.management import call_command
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "banco.settings")
os.environ['FACEBOOK_APP_SECRET'] = 'FACEBOOK_APP_SECRET'
os.environ['FACEBOOK_APP_ID'] = 'FACEBOOK_APP_ID'
call_command('test', verbosity=1)
