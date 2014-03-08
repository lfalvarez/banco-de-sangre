# -*- coding: utf-8 -*-
from django.test import TestCase
from dona_sangre.models import Appointment, FacebookDonor
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
        
        apointment = Appointment.objects.create(donor=self.user, date=tomorrow)


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
