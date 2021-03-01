from django import forms 


class LoginForm (forms.Form):
    username = forms.CharField(
        label= "Username",
        required =True
    )

    password = forms.CharField (
        label = "Password",
        required =True,
        widget = forms.PasswordInput 
    )
