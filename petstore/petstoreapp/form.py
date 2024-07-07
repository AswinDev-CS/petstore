from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from petstoreapp.models import Carts,PlaceOrder


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
        label=''
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
        label=''
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        label=''
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        label=''
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label=''
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}),
        label=''
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
        

class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        label=''
    )
    
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        label=''
    )
    
    
class CartForm(forms.ModelForm):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'rounded-start border border-1 inp',
            'placeholder': 'Count',
            'aria-label': 'Example input',
            'aria-describedby': 'button-addon1',
        })
    )
    class Meta:
        model = Carts
        fields = ['quantity']
        
    
class PlaceOrderForm(forms.ModelForm):
    class Meta:
        model = PlaceOrder
        fields = ["address"]