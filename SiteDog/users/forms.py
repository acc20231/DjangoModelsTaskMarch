from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин",
                               widget=forms.TimeInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))