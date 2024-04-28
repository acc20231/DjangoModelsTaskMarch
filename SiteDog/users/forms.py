from django import forms

class LoginUserForm(forms.Form):
    usernames = forms.CharField(label="Логин",
                               widget=forms.TimeInput(attrs={'class': 'form-input'}))
    passwordd = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))