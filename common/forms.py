from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User
from .models import Parking

"""
기존 클래스
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")
"""

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number','email','car_number')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone_number','email','car_number')

    def clean_password(self):
        return self.initial["password"]


class ParkingCreateForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ('parking_number', 'parking_name', 'lat', 'lon', 'res_state', 'detail_add', 'finish_car_number')