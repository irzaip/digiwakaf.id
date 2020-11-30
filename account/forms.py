from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, Asset
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'first_name','last_name','username', 'email', 'password1', 'password2']
        labels = { 'first_name' : "Nama depan", 
            'email': 'Alamat Surel',
            'last_name': 'Nama Belakang',
            'username': 'Username',
            'password2': 'Konfirmasi Password'}
        help_texts = {'first_name': "Jangan gitu yaa", 'password1': ""}



class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        exclude = ['downloadable', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))        
   