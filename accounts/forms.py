import random
from django import forms

from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'mobile_no',
            'password1',
            'password2',
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"required": "required"}),
            "last_name": forms.TextInput(attrs={"required": "required"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        username = self.cleaned_data.get("username", "")
        if username == "":
            user.username = (
                f'{self.cleaned_data.get("first_name")}\
                {random.randint(1, 1000)}'
            ).strip()
        user.save()
        return user
