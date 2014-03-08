# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractUser
import datetime

class FacebookDonor(AbstractUser, FacebookModel):
	pass

class Appointment(models.Model):
	donor = models.ForeignKey(FacebookDonor)
	date = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(days=1)))
	notes = models.TextField()


