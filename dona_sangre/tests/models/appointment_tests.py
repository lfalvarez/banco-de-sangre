# -*- coding: utf-8 -*-
from django.test import TestCase
from dona_sangre.models import Appointment, FacebookDonor
from django.test.client import Client
from django.core.urlresolvers import reverse
import datetime

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

class AppointmentTestCase(TestCase):
    def setUp(self):
        self.user = FacebookDonor.objects.create(
            facebook_id=1234,
            facebook_name="Feli"
            )

    def test_create_an_appointment(self):
        '''Puedes crear una cita para ir a donar sangre'''
        
        apointment = Appointment.objects.create(donor=self.user, date=tomorrow, \
                        notes="Me regalarán chocolate??")


        self.assertTrue(apointment)
        self.assertEquals(apointment.donor, self.user)
        self.assertEquals(apointment.date, tomorrow)

    def test_an_appointment_has_default_tomorrow(self):
        '''Una cita tiene por defecto la fecha de mañana'''

        apointment = Appointment.objects.create(donor=self.user)
        self.assertEquals(apointment.date.day, tomorrow.day)
        self.assertEquals(apointment.date.month, tomorrow.month)
        self.assertEquals(apointment.date.year, tomorrow.year)
        self.assertEquals(apointment.date.hour, tomorrow.hour)

from dona_sangre.forms import AppointmentModelForm

class AppointmentModelFormTestCase(TestCase):
    def setUp(self):
        self.user = FacebookDonor.objects.create(
            facebook_id=1234,
            facebook_name="Feli"
            )


    def test_create_an_appointment_using_form(self):
        """Puedo crear una cita para ir a donar utilizando un formulario"""
        
        data = {
        'date':tomorrow,
        'notes':u"Hola me llamo juanito y quiero puro donar sangre"
        }
        form = AppointmentModelForm(data, donor=self.user)
        new_appointment = form.save()

        self.assertTrue(new_appointment)
        self.assertEquals(new_appointment.donor, self.user)
        self.assertEquals(new_appointment.date.day, tomorrow.day)
        self.assertEquals(new_appointment.date.month, tomorrow.month)
        self.assertEquals(new_appointment.date.year, tomorrow.year)
        self.assertEquals(new_appointment.date.hour, tomorrow.hour)
        self.assertEquals(new_appointment.notes, u"Hola me llamo juanito y quiero puro donar sangre")

    def test_instanciate_an_appointment_without_donor(self):
        """Puedo instanciar un formulario sin donante"""
        form = AppointmentModelForm()
        self.assertTrue(form)
        self.assertFalse(hasattr(form, 'donor'))

    def test_account_page_contains_the_form(self):
        """La pagina de mi cuenta ya tiene el formulario"""
        c = Client()
        c.login(facebook_id=self.user.facebook_id)
        url = reverse('account')
        response = c.get(url)

        self.assertIn('new_appointment_form', response.context)
        self.assertIsInstance(response.context['new_appointment_form'], AppointmentModelForm)
        self.assertFalse(hasattr(response.context['new_appointment_form'], 'donor'))


