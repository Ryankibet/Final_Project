from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email *'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number *'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message *', 'style': 'width: 100%; height: 150px;'}),
        }
