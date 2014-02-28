# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class HomeTestCase(TestCase):
	def setUp(self):
		self.client = Client()

	def test_get_home_and_render(self):
		"""Obtiene la pagina de incio y la dibuja bacán"""
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'base.html')
		self.assertTemplateUsed(response, 'sangre/home.html')

