#!/usr/bin/env python
from django.core.management import call_command
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "banco.settings")
call_command('test', verbosity=2)
