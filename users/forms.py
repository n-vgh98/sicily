from .models import *
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phone_number', ]
