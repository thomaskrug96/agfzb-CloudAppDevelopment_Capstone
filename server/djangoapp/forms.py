from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import DealerReview


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateReviewForm(forms.Form):
    name = forms.CharField(label='name', max_length=200)
    review = forms.CharField(label='name', max_length=500)
    purchase = forms.BooleanField(required=False)

    def save():
        print('you did it!')

