# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from dona_sangre.models import FacebookDonor


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

    def test_get_home_when_logged_in(self):
        """En la página de inicio incluye al usuario"""
        user = FacebookDonor.objects.create(
            facebook_id=1234
            )
        self.client.login(facebook_id=user.facebook_id)
        url = reverse('home')
        response = self.client.get(url)
        self.assertIn('user', response.context)
        self.assertIsNotNone(response.context['user'])
        self.assertTrue(response.context['user'].is_authenticated())

    def test_get_home_when_not_logged_in(self):
        '''Cuando el usuario no está loggeado en home'''
        url = reverse('home')
        response = self.client.get(url)
        self.assertFalse(response.context['user'].is_authenticated())
