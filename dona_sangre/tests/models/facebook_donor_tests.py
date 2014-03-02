# -*- coding: utf-8 -*-
from django.test import TestCase
from dona_sangre.models import FacebookDonor
from django_facebook.models import FacebookModel, FacebookCustomUser
from django.contrib.auth.models import User
from django_facebook.utils import get_user_model
from django.conf import settings

class FacebookDonorTestCase(TestCase):
	def setUp(self):
		pass

	def test_create_one(self):
		"""Creando un perfil de facebook crea un usuario"""
		user = FacebookCustomUser.objects.create(facebook_name="Feli")
		facebook_donor = FacebookDonor.objects.create(
			user=user,
			facebook_id=1234,
			facebook_name="Feli"
			)

		self.assertTrue(facebook_donor)
		self.assertIsInstance(facebook_donor, FacebookModel)
		self.assertEquals(facebook_donor.facebook_id, 1234)
		self.assertEquals(facebook_donor.facebook_name, "Feli")

	# def test_it_automatically_creates_a_user(self):
	# 	"""Crea automáticamente un perfil de facebook a partir de un usuario"""
	# 	user_model = get_user_model()
	# 	print user_model
	# 	user = user_model.objects.create_user(username='feli', password='alvarez')
	# 	self.assertIsNotNone(user.profile)
	# 	self.assertIsInstance(user.profile, FacebookDonor)
		# facebook_donor = FacebookDonor.objects.create(
		# 	facebook_id=1234,
		# 	facebook_name="Feli"
		# 	)
		
		# self.assertIsNotNone(facebook_donor.user)
		# self.assertIsInstance(facebook_donor.user, User)