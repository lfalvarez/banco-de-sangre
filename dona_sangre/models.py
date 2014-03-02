# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class FacebookDonor(FacebookModel):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")

# @receiver(pre_save, sender=user_model)
# def automatically_create_a_profile(instance, sender, **kwargs):
# 	user = instance
# 	profile, new = FacebookDonor.objects.get_or_create(user=instance)
