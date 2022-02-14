from django import forms
from django.forms import ModelForm

from apps.user.models import User


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # solapin = forms.CharField(max_length=7, min_length=7)

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['groups', 'last_login', 'is_superuser',
                   'is_staff', 'is_active', 'date_joined',
                   'user_permissions']
