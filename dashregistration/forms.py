from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
   
    class Meta:
        model = User
        fields= ['username','first_name','last_name','password1','password2']
    
    
    def __init__(self, *args , **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter username...'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'First name...'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'last name...'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'password 1...'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'password 2...'})
        


