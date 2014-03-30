from django.forms import ModelForm, Textarea, DateInput
from dona_sangre.models import Appointment

class AppointmentModelForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'notes']
        widgets = {
            'date': DateInput(attrs={'class': 'form-control datepicker'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        if 'donor' in kwargs:
            self.user = kwargs.pop('donor')
        super(AppointmentModelForm, self).__init__(*args, **kwargs)

    def save(self):
        appointment = super(AppointmentModelForm, self).save(commit=False)
        appointment.donor = self.user
        appointment.save()
        return appointment