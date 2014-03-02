# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class UserSectionViewsTestCase(TestCase):
	def setUp(self):
		pass

	def test_account_resolves_the_url(self):
		"""Existe la url de mi cuenta"""
		url = reverse("account")

		self.assertTrue(url)

	def test_redirects_to_home_when_not_logged_in(self):
		"""Te redirecciona a la página de inicio si no estás loggeado"""
		c = Client()
		url = reverse('account')
		response = c.get(url)

		home_url = reverse('home') + "?next=" + url
		self.assertRedirects(response, home_url)