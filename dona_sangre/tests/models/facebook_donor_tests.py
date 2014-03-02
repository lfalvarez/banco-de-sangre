# -*- coding: utf-8 -*-
from django.test import TestCase
from dona_sangre.models import FacebookDonor
from django_facebook.models import FacebookModel
from django.contrib.auth.models import User
from django_facebook.utils import get_user_model
from django.conf import settings

import inspect

def get_user_attributes(cls):
    boring = dir(type('dummy', (object,), {}))
    return [item
            for item in inspect.getmembers(cls)
            if item[0] not in boring]

class FacebookDonorTestCase(TestCase):
	def setUp(self):
		pass

	def test_create_one(self):
		"""Creando un perfil de facebook crea un usuario"""
		facebook_donor = FacebookDonor.objects.create(
			facebook_id=1234,
			facebook_name="Feli"
			)

		self.assertTrue(facebook_donor)
		self.assertIsInstance(facebook_donor, FacebookModel)
		self.assertEquals(facebook_donor.facebook_id, 1234)
		self.assertEquals(facebook_donor.facebook_name, "Feli")
		self.assertIsNotNone(facebook_donor.id)