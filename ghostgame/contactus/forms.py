from django import forms
class ticketform(forms.Form):
    name=forms.CharField(max_length=16,widget=forms.TextInput(attrs={'placeholder':'name'}))
    surname=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'surname'}))
    email=forms.EmailField(max_length=256,widget=forms.TextInput(attrs={'placeholder':'email'}))
    subject=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'subject'}))
    message=forms.CharField(max_length=400,widget=forms.Textarea(attrs={'placeholder':'your message'}))