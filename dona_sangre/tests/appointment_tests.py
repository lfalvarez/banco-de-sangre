# -*- coding: utf-8 -*-
from django.test import TestCase
from dona_sangre.models import Appointment, FacebookDonor
from django.test.client import Client
from django.core.urlresolvers import reverse
import datetime
from django.utils.timezone import now, make_aware, get_default_timezone

tomorrow = now() + datetime.timedelta(days=1)

class AppointmentTestCaseMixin(object):
    def setUp(self):
        self.user = FacebookDonor.objects.create(
            facebook_id=1234,
            facebook_name="Feli",
            username="feli"
            )

class AppointmentTestCase(AppointmentTestCaseMixin, TestCase):

    def test_create_an_appointment(self):
        '''Puedes crear una cita para ir a donar sangre'''
        
        apointment = Appointment.objects.create(donor=self.user, date=tomorrow, \
                        notes="Me regalarán chocolate??")


        self.assertTrue(apointment)
        self.assertEquals(apointment.donor, self.user)
        self.assertEquals(apointment.date, tomorrow)
        self.assertIn(apointment, self.user.appointments.all())

    def test_an_appointment_has_default_tomorrow(self):
        '''Una cita tiene por defecto la fecha de mañana'''

        apointment = Appointment.objects.create(donor=self.user)
        self.assertEquals(apointment.date.day, tomorrow.day)
        self.assertEquals(apointment.date.month, tomorrow.month)
        self.assertEquals(apointment.date.year, tomorrow.year)
        self.assertEquals(apointment.notes, u"")

    def test_appointment_unicode(self):
        '''Una cita tiene unicode method'''
        date = datetime.date(2007, 12, 5)
        apointment = Appointment.objects.create(donor=self.user, date=date)
        en_unicode = apointment.__unicode__()

        self.assertIn(u'5/12/2007', en_unicode)

    def test_get_absolute_url(self):
        """Una cita tiene su página aparte"""
        apointment = Appointment.objects.create(donor=self.user)
        url = apointment.get_absolute_url()
        self.assertTrue(url)
        c = Client()
        c.login(facebook_id=self.user.facebook_id)
        response = c.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertIn('appointment', response.context)
        self.assertEquals(response.context['appointment'], apointment)
        self.assertTemplateUsed(response, 'sangre/appointment.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_not_owner_cannot_access_appointment_detail(self):
        '''Una persona que no es dueña no puede acceder a la cita'''
        not_owner = FacebookDonor.objects.create(
            facebook_id=456,
            facebook_name=u"no soy el dueño",
            username="not_owner"
            )
        apointment = Appointment.objects.create(donor=self.user)
        c = Client()
        c.login(facebook_id=not_owner.facebook_id)
        response = c.get(apointment.get_absolute_url())
        self.assertEquals(response.status_code, 404)

    def test_not_logged_accessing_an_appointment(self):
        '''Un usuario sin login no puede ver una cita'''
        not_owner = FacebookDonor.objects.create(
            facebook_id=456,
            facebook_name=u"no soy el dueño",
            username="not_owner"
            )
        apointment = Appointment.objects.create(donor=self.user)
        c = Client()
        #not logged user
        response = c.get(apointment.get_absolute_url())
        self.assertEquals(response.status_code, 404)


from dona_sangre.forms import AppointmentModelForm

class AppointmentModelFormTestCase(AppointmentTestCaseMixin, TestCase):

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

class NewAppointmentView(AppointmentTestCaseMixin, TestCase):
    def test_post_url_is_accessible(self):
        """La url para crear una cita existe"""
        url = reverse('create_appointment')
        self.assertTrue(url)

    def test_when_I_post_as_a_logged_user_it_creates_the_apointment(self):
        """Cuando estoy logeado puedo postear los datos y crearme una cita"""
        c = Client()
        c.login(facebook_id=self.user.facebook_id)

        data = {
        'date':'2014-03-30',
        'notes':u"Hola me llamo juanito y quiero puro donar sangre"
        }
        url = reverse('create_appointment')
        response = c.post(url, data=data)
        appointment = Appointment.objects.get(donor=self.user)
        self.assertRedirects(response, appointment.get_absolute_url())

        
        self.assertTrue(appointment)
        self.assertEquals(appointment.notes, data['notes'])

    def test_mistakes_in_the_form(self):
        '''Cuando cometo errores en el formulario me lo redibuja'''
        c = Client()
        c.login(facebook_id=self.user.facebook_id)

        data = {
        'date':'Esto no es una fecha',
        'notes':u"Hola me llamo juanito y quiero puro donar sangre"
        }
        url = reverse('create_appointment')
        response = c.post(url, data=data)
        self.assertTrue(response.context['new_appointment_form'].errors)
        self.assertTrue(response.context['new_appointment_form'].errors['date'])

    def test_when_Im_not_logged_I_get_redirect(self):
        '''Cuando no estoy loggeado me pide que me loguinee'''
        c = Client()
        data = {
        'date':'2014-03-30',
        'notes':u"Hola me llamo juanito y quiero puro donar sangre"
        }
        url = reverse('create_appointment')
        response = c.post(url, data=data)
        self.assertRedirects(response, '/?next=/create_appointment')

