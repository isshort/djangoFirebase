from django import forms

from blog.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password','email','phone','first_name','last_name']
