# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from dona_sangre.models import FacebookDonor

class UserSectionViewsTestCase(TestCase):
    def setUp(self):
        self.user = FacebookDonor.objects.create(
            facebook_id=1234
            )

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

    def test_I_can_loggin_with_a_facebook_user(self):
        c = Client()
        
        login = c.login(facebook_id=self.user.facebook_id)
        self.assertTrue(login)

    def test_the_url_exists_and_is_reachable_when_logged(self):
        c = Client()
        c.login(facebook_id=self.user.facebook_id)
        url = reverse('account')
        response = c.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "sangre/your-profile.html")
        self.assertTemplateUsed(response, "base.html")
