from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput, Select, RadioSelect

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))

from django.forms import ModelForm
from app.models import Event, Reservation
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

BootstrapTextInput = TextInput(attrs={'class': 'form-control'})
BootstrapSelect = Select(attrs={'class': 'form-select'})


class CustomDatePickerInput(DatePickerInput):
    template_name = 'widgets/custom-bootstrap-date-time-picker.html'
class CustomTimePickerInput(TimePickerInput):
    template_name = 'widgets/custom-bootstrap-date-time-picker.html'

class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.name:
            self.fields['name'].widget.attrs['readonly'] = True

    class Meta:
        model = Event
        fields = ['name', 'date', 'time']
        widgets = {
            'name': BootstrapTextInput,
            'date': CustomDatePickerInput(format='%d.%m.%Y'),
            'time': CustomTimePickerInput()
        }

class ReservationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.email and instance.event:
            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['event'].widget.attrs['style'] = 'background-color: #e9ecef; opacity: 1; pointer-events: none; touch-actions: none;'     

    class Meta:
        model = Reservation
        fields = ['event', 'email', 'surname', 'name', 'zipcode', 'phone', 'proof', 'entry']
        widgets = {
            'event': BootstrapSelect,
            'email': BootstrapTextInput,
            'surname': BootstrapTextInput,
            'name': BootstrapTextInput,
            'zipcode': BootstrapTextInput,
            'phone': BootstrapTextInput,
            'proof': BootstrapSelect,
            'entry': RadioSelect()
        }