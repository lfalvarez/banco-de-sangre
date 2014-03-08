from django.forms import ModelForm
from dona_sangre.models import Appointment

class AppointmentModelForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'notes']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('donor')
        super(AppointmentModelForm, self).__init__(*args, **kwargs)

    def save(self):
        appointment = super(AppointmentModelForm, self).save(commit=False)
        appointment.donor = self.user
        appointment.save()
        return appointment