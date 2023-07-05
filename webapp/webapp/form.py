from django import forms

class loginPage(forms.Form):
    username = forms.CharField(label="UserName", max_length=50,widget=forms.TextInput(attrs={'class':"form-group"}))
    password = forms.CharField(label="Contact Number ", max_length=11,widget=forms.TextInput(attrs={'class':"form-group"}))
    email = forms.EmailField(label="Email Address",widget=forms.EmailInput(attrs={'class':"form-group"}))
    Remember_me = forms.Field(label="Remember me ",widget=forms.CheckboxInput())