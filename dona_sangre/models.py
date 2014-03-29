# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractUser
import datetime
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from django.utils.translation import ugettext as _

class FacebookDonor(AbstractUser, FacebookModel):
	pass

class Appointment(models.Model):
	donor = models.ForeignKey(FacebookDonor, related_name='appointments')
	date = models.DateField(default=(now() + datetime.timedelta(days=1)))
	notes = models.TextField(default=u"")

	def get_absolute_url(self):
		return reverse('appointment_detail', kwargs={'pk':self.pk})

	def __unicode__(self):
		result =  _(u"%(date)s"%{
			'date':self.date.date().strftime('%d/%m/%Y')
			})

		return result

