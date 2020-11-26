from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'first_name','last_name','username', 'email', 'password1', 'password2']
        labels = { 'first_name' : "Haha Name", 'email': 'Alamat Surel'}
        help_texts = {'first_name': "Jangan gitu yaa", 'password': ""}
   