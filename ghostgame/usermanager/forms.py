from django import forms 
from django.contrib.auth.models import User
class userRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'username'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email@example.com'}))
    firstname=forms.CharField(max_length=30)
    lastname=forms.CharField(max_length=40)
    password1=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'placeholder':'password 2'}))
#-----------------------------------------------------------
    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError("username taken")
        else:return user
#-----------------------------------------------------------
    def clean_email(self):
        mail=self.cleaned_data['email']
        if User.objects.filter(email=mail).exists():
            raise forms.ValidationError("email used")
        else: return mail
#-----------------------------------------------------------
    def clean_password2(self):
        pass1=self.cleaned_data['password1']
        pass2=self.cleaned_data['password2']
        if pass1!=pass2:
            raise forms.ValidationError('password not match')
        elif len(pass1)<8:
            raise forms.ValidationError('password atleast have 8 character')
        elif not any(char.isdigit() for char in pass1)or not any(char.isalpha() for char in pass1):
            raise forms.ValidationError('must contain letters and numbers')
        elif not any(i.isupper() for i in pass1):
            raise forms.ValidationError("atleast on of the characters should be upper")
        else: 
            return pass1
        
class userLoginForm(forms.Form):
    user=forms.CharField(max_length=30)
    password=forms.CharField(max_length=16)
class ChangePasswordForm(forms.Form):
    old_pass=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'placeholder':'oldpassword'}))
    new_pass1=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'placeholder':'newpassword 1'}))
    new_pass2=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'placeholder':'newpassword2'}))