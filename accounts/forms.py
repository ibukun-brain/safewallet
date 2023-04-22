from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email',
            'mobile_no'
            'date_of_birth',
            'password1',
            'password2',
        ]
    

        widgets = {
            "first_name": forms.TextInput(attrs={"required":"required"}),
            "last_name": forms.TextInput(attrs={"required":"required"}),
            "date_of_birth": forms.DateInput(attrs={"type":"date"})
        }
