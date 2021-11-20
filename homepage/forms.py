from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# HTML attributes for input fields
ATTRS = {
    'username': {
        'class': 'bg-dark form-control form-control-user',
        'type': 'username',
        'id': 'exampleInputUsername',
        'aria-describedby': 'usernameHelp',
        'placeholder': 'Username',
        'name': 'username',
        'maxlength': '35'
    },
    'email': {
        'class': 'bg-dark form-control form-control-user',
        'type': 'email',
        'id': 'exampleInputEmail',
        'aria-describedby': 'emailHelp',
        'placeholder': 'Email',
        'name': 'email'
    },
    'password1': {
        'class': 'bg-dark form-control form-control-user',
        'type': 'password',
        'id': 'examplePasswordInput',
        'placeholder': 'Password',
        'name': 'password'
    },
    'password2': {
        'class': 'bg-dark form-control form-control-user',
        'type': 'password',
        'id': 'exampleRepeatPasswordInput',
        'placeholder': 'Repeat Password',
        'name': 'password_repeat'
    }
}

class UserRegisterForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(ATTRS['username'])
        self.fields['password1'].widget.attrs.update(ATTRS['password1'])
        self.fields['password2'].widget.attrs.update(ATTRS['password2'])
    
    email = forms.EmailField(widget=forms.TextInput(attrs=ATTRS['email']))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

