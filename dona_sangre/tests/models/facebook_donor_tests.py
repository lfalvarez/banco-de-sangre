# -*- coding: utf-8 -*-
from django.test import TestCase
from dona_sangre.models import FacebookDonor
from django_facebook.models import FacebookModel

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