from django.forms import ModelForm

from apps.user.models import User


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['groups', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
